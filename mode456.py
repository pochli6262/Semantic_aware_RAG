"""
4
RETRIEVAL_MODE=2 python3 mode456.py

5
RETRIEVAL_MODE=3 python3 mode456.py

6
RETRIEVAL_MODE=4 python3 mode456.py
"""


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

SOURCE_DIR = "Code_new"                 # 原始程式碼根目錄
PROBLEM_DIR = "problems"                # 題目描述根目錄

MODEL_ID = "gpt-5-mini"                 # 修復用模型
EMBED_MODEL = "text-embedding-3-small"  # 檢索用 embedding 模型

OUTPUT_DIR = f"repaired_programs_{MODEL_ID}_baseline"
RAW_OUTPUT_DIR = f"raw_outputs_{MODEL_ID}_baseline"
FAILED_LOG = f"failed_files_{MODEL_ID}_baseline.txt"

MAX_RETRIES = 3
FINAL_TOPK = 5        
DIFF_MAX_CHARS = 4000
MAX_CODE_LINES = 200

DOC_FILE = "documents.jsonl"

# === 實驗控制 ===
RETRIEVAL_MODE = int(os.getenv("RETRIEVAL_MODE", "1"))

FAISS_FILES = {
    2: "faiss2.index",  # 只程式碼
    3: "faiss3.index",  # 描述+程式 串接
    4: "faiss4.index",  # 描述與程式 concat
}

openai.api_key = API_KEY
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RAW_OUTPUT_DIR, exist_ok=True)

# ===================== 載入 RAG index + 文件 =====================
faiss_file = FAISS_FILES.get(RETRIEVAL_MODE)
if not (faiss_file and os.path.exists(faiss_file)):
    raise FileNotFoundError(f"找不到對應索引：{faiss_file}，請先執行 build_faiss_all_modes.py")

if not os.path.exists(DOC_FILE):
    raise FileNotFoundError(f"找不到 {DOC_FILE}")

print(f"📂 載入 FAISS: {faiss_file}")
index = faiss.read_index(faiss_file)

with open(DOC_FILE, "r", encoding="utf-8") as f:
    docs = [json.loads(line) for line in f]

# ===================== 小工具 =====================
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

def truncate_code_for_embedding(code: str, max_lines: int = MAX_CODE_LINES) -> str:
    lines = code.splitlines()
    if len(lines) > max_lines:
        half = max_lines // 2
        return "\n".join(lines[:half] + ["... [truncated] ..."] + lines[-half:])
    return code

def truncate_text(s: str, limit: int) -> str:
    if s is None:
        return ""
    return s if len(s) <= limit else (s[:limit] + f"\n... [TRUNCATED {len(s)-limit} chars]")

def get_embedding(text: str):
    text = text if text is not None else ""
    text = re.sub(r"\s+", " ", text).strip()
    resp = openai.embeddings.create(model=EMBED_MODEL, input=text)
    return np.array(resp.data[0].embedding, dtype="float32")

# ===================== 檢索 =====================
def retrieve_candidates(description: str, code: str, top_k: int = FINAL_TOPK):
    snippet = truncate_code_for_embedding(code, MAX_CODE_LINES)

    if RETRIEVAL_MODE == 1:
        qvec = get_embedding(description)
    elif RETRIEVAL_MODE == 2:
        qvec = get_embedding(snippet)
    elif RETRIEVAL_MODE == 3:
        qvec = get_embedding(description + "\n\n" + snippet)
    elif RETRIEVAL_MODE == 4:
        qvec = np.concatenate([get_embedding(description), get_embedding(snippet)]).astype("float32")
    else:
        raise ValueError(f"Unknown RETRIEVAL_MODE={RETRIEVAL_MODE}")

    q = qvec.reshape(1, -1)
    D, I = index.search(q, top_k)
    return [docs[i] for i in I[0] if 0 <= i < len(docs)]

# ===================== 修復 Prompt =====================
def build_repair_prompt(code: str, description: str, diffs: list[str]) -> str:
    diffs_block = "\n\n".join(
        [f"### Diff {i+1}\n{truncate_text(d, DIFF_MAX_CHARS)}" for i, d in enumerate(diffs)]
    ) if diffs else "No diffs retrieved."

    return f"""
You are a Python expert.

A user gives you the following Python program which is buggy.

## Problem Description (from dataset)
{description}

## Buggy Program
{code}

## Related Known Fixes (retrieved diffs)
{diffs_block}

Your task:
1) Identify the single incorrect line according to the problem description and the retrieved diffs.
2) Assume EXACTLY ONE line is wrong.
3) Provide the corrected version of the ENTIRE program, changing only that single line — all other lines must remain identical.
4) Do not restructure or rewrite unrelated code.
5) Respond ONLY in JSON format:

{{
  "explanation": "Explain what was wrong in that single line and how you fixed it.",
  "fixed_code": "The FULL program with only that ONE line corrected."
}}
""".strip()

# ===================== 主流程 =====================
def repair_file(src_path: str, desc_path: str, out_dir: str):
    out_json_path = os.path.join(out_dir, "faultyVersion.json")
    out_py_path   = os.path.join(out_dir, "faultyVersion.py")

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

    # 檢索
    candidates = retrieve_candidates(description, code, top_k=FINAL_TOPK)
    diffs = [c.get("diff", "") for c in candidates if c.get("diff")]

    # 修復
    prompt = build_repair_prompt(code, description, diffs)
    ensure_dir(os.path.join(out_dir, "repair_prompt.txt"))
    with open(os.path.join(out_dir, "repair_prompt.txt"), "w", encoding="utf-8") as fpr:
        fpr.write(prompt)

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

# ===================== 掃描並執行 =====================
if __name__ == "__main__":
    for dirpath, _, filenames in os.walk(SOURCE_DIR):
        if "faultyVersion.py" not in filenames:
            continue

        src_path = os.path.join(dirpath, "faultyVersion.py")

        # 題目名稱
        problem_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(src_path))))
        desc_path = os.path.join(PROBLEM_DIR, problem_name, "statement.md")

        # 鏡像 Code_new 的結構輸出
        rel_dir = os.path.relpath(dirpath, SOURCE_DIR)
        mirror_out_dir = os.path.join(OUTPUT_DIR, rel_dir)

        repair_file(src_path, desc_path, mirror_out_dir)
