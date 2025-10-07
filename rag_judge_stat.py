#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
import csv
import faiss
import numpy as np
import openai

# ===================== 設定 =====================
API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

SOURCE_DIR = "Code_new"
ORACLE_FILE = "oracle_summaries.json"
GEN_SUMMARY_ROOT = os.getenv("GEN_SUMMARY_ROOT", "repaired_programs_gpt-4o-mini_exp8")
DOC_FILE = "documents.jsonl"
OUTPUT_CSV = "rag_judge_results_gpt-4o-mini_exp8.csv"
OUTPUT_ROOT = "rag_sum_gpt-4o-mini_exp8"

MODEL_ID = "gpt-4o-mini"
EMBED_MODEL = "text-embedding-3-small"
FINAL_TOPK = 5
MAX_CODE_LINES = 200
DIFF_MAX_CHARS = 3000

SUMMARY_MODE = os.getenv("SUMMARY_MODE", "oracle")
# oracle / generated / none

RETRIEVAL_MODE = int(os.getenv("RETRIEVAL_MODE", "2"))
# 2: code-only
# 3: summary+code concat
# 4: summary embedding concat code embedding

FAISS_FILES = {
    2: "faiss2.index",
    3: "faiss3.index",
    4: "faiss4.index",
}

openai.api_key = API_KEY

# ===================== 載入資料 =====================
faiss_file = FAISS_FILES.get(RETRIEVAL_MODE)
if not (faiss_file and os.path.exists(faiss_file)):
    raise FileNotFoundError(f"❌ 找不到 {faiss_file}")

print(f"📂 載入 FAISS: {faiss_file}")
index = faiss.read_index(faiss_file)

with open(DOC_FILE, "r", encoding="utf-8") as f:
    docs = [json.loads(line) for line in f]

if os.path.exists(ORACLE_FILE):
    with open(ORACLE_FILE, "r", encoding="utf-8") as f:
        oracle_summaries = json.load(f)
else:
    oracle_summaries = {}

# ===================== 工具 =====================
def truncate_code(code: str, max_lines: int = MAX_CODE_LINES):
    lines = code.splitlines()
    if len(lines) > max_lines:
        half = max_lines // 2
        return "\n".join(lines[:half] + ["... [truncated] ..."] + lines[-half:])
    return code

def truncate_text(s: str, limit: int):
    if s is None:
        return ""
    return s if len(s) <= limit else (s[:limit] + f"\n... [TRUNCATED {len(s)-limit} chars]")

def get_embedding(text: str):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        text = "(empty)"
    resp = openai.embeddings.create(model=EMBED_MODEL, input=text)
    return np.array(resp.data[0].embedding, dtype="float32")

def retrieve_candidates(summary: str, code: str, top_k: int = FINAL_TOPK):
    snippet = truncate_code(code, MAX_CODE_LINES)

    if RETRIEVAL_MODE == 1:
        qvec = get_embedding(summary)
    elif RETRIEVAL_MODE == 2:
        qvec = get_embedding(snippet)
    elif RETRIEVAL_MODE == 3:
        qvec = get_embedding(summary + "\n\n" + snippet)
    elif RETRIEVAL_MODE == 4:
        qvec = np.concatenate([get_embedding(summary), get_embedding(snippet)]).astype("float32")
    else:
        raise ValueError(f"Unknown RETRIEVAL_MODE={RETRIEVAL_MODE}")

    D, I = index.search(qvec.reshape(1, -1), top_k)
    return [docs[i] for i in I[0] if 0 <= i < len(docs)]

def build_judge_prompt(task_id, buggy_code, oracle_summary, candidates):
    retrieved_blocks = []
    for i, c in enumerate(candidates, 1):
        retrieved_blocks.append(
            f"### Candidate {i}\nSummary: {c.get('problem','')}\nDiff:\n{truncate_text(c.get('diff',''), DIFF_MAX_CHARS)}"
        )
    retrieved_text = "\n\n".join(retrieved_blocks)

    return f"""
You are a Python bug classification assistant.

We are analyzing a buggy program and retrieved candidate fixes.

## Query (ground-truth bug)
Task ID: {task_id}
Buggy Program:
{buggy_code}

Oracle Bug Summary (for judging relevance):
{oracle_summary}

## Retrieved Candidates
{retrieved_text}

Task:
For each retrieved candidate, decide if it is "useful" for fixing the query bug.

A candidate should be considered useful if:
- It belongs to the same bug type (see the 10 categories below), OR
- It provides any partial inspiration, idea, or related repair strategy that could help the developer think about the correct fix, even if it is not an exact match, OR
- It highlights relevant code areas or shows a similar repair context.

Do NOT count as useful if the candidate is completely unrelated.

Bug Categories (for reference, not strict rules):
1. Off-by-one / Boundary condition
2. Comparison operator error
3. Variable misuse / assignment error
4. Condition inversion / missing branch
5. I/O formatting error
6. Math / modulus error
7. String / formatting error
8. Data structure / initialization error
9. DP / algorithm transition error
10. Hardcoding / missing special case

Return ONLY a JSON list of indices (1-based). Example:
[1, 3, 5]
"""

def analyze_with_gpt(task_id, buggy_code, oracle_summary, candidates):
    prompt = build_judge_prompt(task_id, buggy_code, oracle_summary, candidates)
    resp = openai.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    content = resp.choices[0].message.content.strip()
    if content.startswith("```"):
        content = content.strip("`").replace("json", "").strip()
    try:
        result = json.loads(content)
        return result if isinstance(result, list) else []
    except Exception:
        return []

# ===================== 主流程 =====================
# 建立 processed set 避免重複
processed = set()
if os.path.exists(OUTPUT_CSV):
    with open(OUTPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            processed.add(row["task"])
else:
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["task", "useful_diffs_count", "useful_diffs_indices"])

for dirpath, _, filenames in os.walk(SOURCE_DIR):
    if "faultyVersion.py" not in filenames:
        continue

    task_id = os.path.relpath(dirpath, SOURCE_DIR)

    if task_id in processed:
        print(f"⏩ Skip {task_id}, already processed.")
        continue

    print(f"🔎 Analyzing {task_id} ...")

    with open(os.path.join(dirpath, "faultyVersion.py"), "r", encoding="utf-8") as f:
        buggy_code = f.read()

    # --- 檢索 summary 來源 (query_summary) ---
    if SUMMARY_MODE == "oracle":
        if task_id not in oracle_summaries:
            print(f"⚠️ No oracle summary for {task_id}, skip.")
            continue
        query_summary = oracle_summaries[task_id]

    elif SUMMARY_MODE == "generated":
        sum_path = os.path.join(GEN_SUMMARY_ROOT, task_id, "problem_summary.txt")
        if not os.path.exists(sum_path):
            print(f"⚠️ No generated summary for {task_id}, skip.")
            continue
        with open(sum_path, "r", encoding="utf-8") as sf:
            query_summary = sf.read().strip()

    elif SUMMARY_MODE == "none":
        query_summary = ""
    else:
        raise ValueError(f"❌ Unknown SUMMARY_MODE={SUMMARY_MODE}")

    # --- 一律用 oracle summary 做 judge ---
    oracle_summary = oracle_summaries.get(task_id, "")

    # --- 檢索 ---
    candidates = retrieve_candidates(query_summary, buggy_code, top_k=FINAL_TOPK)
    useful_diffs = analyze_with_gpt(task_id, buggy_code, oracle_summary, candidates)

    # --- mirror 存檔 ---
    out_dir = os.path.join(OUTPUT_ROOT, task_id)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "retrieved.json"), "w", encoding="utf-8") as fout:
        json.dump({
            "task": task_id,
            "query_summary": query_summary,   # 用來檢索
            "oracle_summary": oracle_summary, # 用來 judge
            "retrieved": [{"summary": c.get("problem", ""), "diff": c.get("diff", "")} for c in candidates],
            "useful_diffs_indices": useful_diffs,
            "useful_diffs_count": len(useful_diffs)
        }, fout, ensure_ascii=False, indent=2)

    with open(OUTPUT_CSV, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([task_id, len(useful_diffs), useful_diffs])

    print(f"✅ {task_id}: {len(useful_diffs)} useful diffs → {useful_diffs}")

# ===================== 統計 =====================
with open(OUTPUT_CSV, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

total_tasks = len(rows)
if total_tasks > 0:
    hit_at_5 = sum(1 for r in rows if int(r["useful_diffs_count"]) > 0)
    precision_at_5 = sum(int(r["useful_diffs_count"]) / 5.0 for r in rows) / total_tasks
    avg_useful = sum(int(r["useful_diffs_count"]) for r in rows) / total_tasks
else:
    hit_at_5 = precision_at_5 = avg_useful = 0

print("\n📊 Retrieval Quality Stats")
print(f"Total tasks: {total_tasks}")
print(f"Hit@5: {hit_at_5/total_tasks:.3f}" if total_tasks > 0 else "Hit@5: N/A")
print(f"Precision@5: {precision_at_5:.3f}")
print(f"Avg useful diffs per query: {avg_useful:.3f}")

print("🎯 Done. Results stored in", OUTPUT_CSV)
