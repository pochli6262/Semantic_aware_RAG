#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
import faiss
import numpy as np
import openai

# ===================== 設定 =====================
API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")
DOC_FILE = "documents_new.jsonl"   # 每筆 {buggy_code, correct_code}
INDEX_FILE = "faiss2.index"

MODEL_ID = "gpt-5-mini"                # 修復用模型
EMBED_MODEL = "text-embedding-3-small"  # 檢索用 embedding 模型

OUTPUT_DIR = f"repaired_programs_{MODEL_ID}_no_problems"
RAW_OUTPUT_DIR = f"raw_outputs_{MODEL_ID}_no_problems"
FAILED_LOG = f"failed_files_{MODEL_ID}_no_problems.txt"

MAX_RETRIES = 3
FINAL_TOPK = 3
MAX_LINES = 400  # buggy+correct 總行數限制

openai.api_key = API_KEY
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RAW_OUTPUT_DIR, exist_ok=True)

# ===================== 工具函數 =====================
def truncate_code_for_embedding(code: str, max_lines: int = 200) -> str:
    """避免超長程式碼進 embedding"""
    lines = code.splitlines()
    if len(lines) > max_lines:
        half = max_lines // 2
        return "\n".join(lines[:half] + ["... [truncated] ..."] + lines[-half:])
    return code

def get_embedding(text: str):
    """呼叫 OpenAI Embedding API"""
    text = text if text is not None else ""
    text = re.sub(r"\s+", " ", text).strip()
    resp = openai.embeddings.create(model=EMBED_MODEL, input=text)
    return np.array(resp.data[0].embedding, dtype="float32")

def extract_json_best_effort(raw: str):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                return None
    return None

def ensure_dir(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)

# ===================== 建立索引 =====================
def build_faiss_index():
    with open(DOC_FILE, "r", encoding="utf-8") as f:
        docs = [json.loads(line) for line in f]

    embs = []
    for d in docs:
        buggy = d.get("buggy_code", "")
        vec = get_embedding(truncate_code_for_embedding(buggy))
        embs.append(vec)

    emb_mat = np.vstack(embs).astype("float32")
    dim = emb_mat.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(emb_mat)

    faiss.write_index(index, INDEX_FILE)
    print(f"✅ Index 建立完成，共 {len(docs)} 筆")

# ===================== 載入索引 =====================
def load_index():
    if not os.path.exists(INDEX_FILE):
        print("⚠️ 未找到索引，開始建立...")
        build_faiss_index()
    index = faiss.read_index(INDEX_FILE)
    with open(DOC_FILE, "r", encoding="utf-8") as f:
        docs = [json.loads(line) for line in f]
    return index, docs

# ===================== 檢索 =====================
def retrieve_examples(query_code: str, index, docs, top_k=FINAL_TOPK):
    qvec = get_embedding(truncate_code_for_embedding(query_code)).reshape(1, -1)
    D, I = index.search(qvec, top_k * 2)  # 多抓幾筆，避免跳過後不足
    results = []
    for idx in I[0]:
        if 0 <= idx < len(docs):
            buggy = docs[idx].get("buggy_code", "").splitlines()
            correct = docs[idx].get("correct_code", "").splitlines()
            if len(buggy) + len(correct) <= MAX_LINES:
                results.append(docs[idx])
        if len(results) >= top_k:
            break
    return results

# ===================== 建立修復 Prompt =====================
def build_repair_prompt(code: str, description: str, examples: list) -> str:
    example_blocks = []
    for i, ex in enumerate(examples, 1):
        example_blocks.append(
            f"### Example {i}\n"
            f"--- Buggy Code ---\n{ex['buggy_code']}\n\n"
            f"--- Correct Code ---\n{ex['correct_code']}\n"
        )
    examples_text = "\n\n".join(example_blocks) if examples else "No examples retrieved."

    return f"""
You are a Python repair assistant.

A user gives you the following buggy program.

## Buggy Program
{code}

## Related Example Fixes (retrieved from similar problems)
These examples are only references. 
They must NOT be copied directly, but can inspire how similar bugs were fixed.

{examples_text}

Your task:
1) Identify the single incorrect line in the buggy program.
2) Assume EXACTLY ONE line is wrong.
3) Provide the corrected version of the ENTIRE program, changing only that single line.
4) Do not restructure or rewrite unrelated code.
5) Respond ONLY in JSON format:

{{
  "explanation": "Explain the bug and how you fixed it.",
  "fixed_code": "The FULL program with only that ONE line corrected."
}}
""".strip()

# ===================== 主流程 =====================
def repair_file(src_path: str, desc_path: str, out_dir: str, index, docs):
    out_json_path = os.path.join(out_dir, "faultyVersion.json")
    out_py_path = os.path.join(out_dir, "faultyVersion.py")

    if os.path.exists(out_json_path) and os.path.exists(out_py_path):
        print(f"⏭️ 已存在修復檔案，跳過：{src_path}")
        return True

    with open(src_path, "r", encoding="utf-8") as f:
        code = f.read()

    description = ""
    if os.path.exists(desc_path):
        with open(desc_path, "r", encoding="utf-8") as f:
            description = f.read().strip()
    if not description:
        description = "(No problem statement found)"

    print(f"🔍 desc_path={desc_path}, 前50字={description[:50]}")

    # 檢索最相近的程式
    examples = retrieve_examples(code, index, docs, top_k=FINAL_TOPK)

    # 構建 prompt
    prompt = build_repair_prompt(code, description, examples)
    ensure_dir(os.path.join(out_dir, "repair_prompt.txt"))
    with open(os.path.join(out_dir, "repair_prompt.txt"), "w", encoding="utf-8") as fpr:
        fpr.write(prompt)

    # 呼叫模型
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = openai.chat.completions.create(
                model=MODEL_ID,
                messages=[{"role": "user", "content": prompt}]
            )
            content = resp.choices[0].message.content

            raw_try_path = os.path.join(
                RAW_OUTPUT_DIR,
                os.path.relpath(out_dir, OUTPUT_DIR),
                f"try{attempt}.txt"
            )
            ensure_dir(raw_try_path)
            with open(raw_try_path, "w", encoding="utf-8") as fout:
                fout.write(content)

            result = extract_json_best_effort(content)
            if result and "fixed_code" in result:
                ensure_dir(out_json_path)
                with open(out_json_path, "w", encoding="utf-8") as jout:
                    json.dump(result, jout, ensure_ascii=False, indent=2)
                with open(out_py_path, "w", encoding="utf-8") as fpy:
                    fpy.write(result["fixed_code"])
                print(f"✅ 修復完成：{src_path}")
                return True
            else:
                print(f"⚠️ 第 {attempt} 次 JSON 解析失敗：{src_path}")
        except Exception as e:
            print(f"🔥 第 {attempt} 次 API 錯誤：{src_path}: {e}")

    with open(FAILED_LOG, "a", encoding="utf-8") as flog:
        flog.write(src_path + "\n")
    print(f"❌ 放棄修復：{src_path}")
    return False

# ===================== 執行 =====================
if __name__ == "__main__":
    index, docs = load_index()
    for dirpath, _, filenames in os.walk("Code_new"):
        if "faultyVersion.py" not in filenames:
            continue

        src_path = os.path.join(dirpath, "faultyVersion.py")
        problem_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(src_path))))
        desc_path = os.path.join("problems", problem_name, "statement.md")
        rel_dir = os.path.relpath(dirpath, "Code_new")
        mirror_out_dir = os.path.join(OUTPUT_DIR, rel_dir)

        repair_file(src_path, desc_path, mirror_out_dir, index, docs)
