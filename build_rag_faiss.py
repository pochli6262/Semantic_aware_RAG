#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import numpy as np
import faiss
import re
from tqdm import tqdm
import openai

# ===================== 設定 =====================
API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")
DOC_FILE = "documents.jsonl"    # 每行一筆 {problem, buggy_code, diff, ...}
EMBED_MODEL = "text-embedding-3-small"

# 產物
EMB_FILES  = {
    1: "embeddings1.npy",   # desc
    2: "embeddings2.npy",   # code
    3: "embeddings3.npy",   # desc+code (same encoder)
    4: "embeddings4.npy",   # concat(desc_emb, code_emb)
}
FAISS_FILES = {
    1: "faiss1.index",
    2: "faiss2.index",
    3: "faiss3.index",
    4: "faiss4.index",
}

# 其他
MAX_CODE_LINES = 200  # 長程式做截斷避免 embedding 太長

openai.api_key = API_KEY

def truncate_code_for_embedding(code: str, max_lines: int = MAX_CODE_LINES) -> str:
    if not code:
        return ""
    lines = code.splitlines()
    if len(lines) > max_lines:
        half = max_lines // 2
        return "\n".join(lines[:half] + ["... [truncated] ..."] + lines[-half:])
    return code

def get_embedding(text: str):
    text = text if text is not None else ""
    # 清掉多重空白，避免太雜
    text = re.sub(r"\s+", " ", text).strip()
    resp = openai.embeddings.create(model=EMBED_MODEL, input=text)
    return np.array(resp.data[0].embedding, dtype="float32")

def build_one_mode(mode: int, docs_iter):
    """
    mode=1: desc
    mode=2: code
    mode=3: desc + "\n\n" + code
    mode=4: concat(emb(desc), emb(code))
    """
    embs = []
    for doc in docs_iter:
        desc = doc.get("problem", "") or ""
        code = truncate_code_for_embedding(doc.get("buggy_code", "") or "")

        if mode == 1:
            vec = get_embedding(desc)
        elif mode == 2:
            vec = get_embedding(code)
        elif mode == 3:
            vec = get_embedding(desc + "\n\n" + code)
        elif mode == 4:
            ed = get_embedding(desc)
            ec = get_embedding(code)
            vec = np.concatenate([ed, ec]).astype("float32")
        else:
            raise ValueError("Unknown mode")

        embs.append(vec)

    if not embs:
        raise RuntimeError("No embeddings created.")

    emb_mat = np.vstack(embs).astype("float32")
    # 這裡採用 L2 距離（與查詢端一致）
    dim = emb_mat.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(emb_mat)

    np.save(EMB_FILES[mode], emb_mat)
    faiss.write_index(index, FAISS_FILES[mode])

    return emb_mat.shape

if __name__ == "__main__":
    if not os.path.exists(DOC_FILE):
        raise FileNotFoundError(f"找不到 {DOC_FILE}")

    # 先把 jsonl 都讀進來一次，避免重複 IO
    with open(DOC_FILE, "r", encoding="utf-8") as f:
        all_docs = [json.loads(line) for line in f]

    print(f"共載入 {len(all_docs)} 筆文件。開始建立四種索引…")

    for mode in (1, 2, 3, 4):
        print(f"\n=== 構建 mode {mode} 的索引 ===")
        shape = build_one_mode(mode, tqdm(all_docs, desc=f"Mode {mode}"))
        print(f"完成 mode {mode}: 向量矩陣形狀 {shape}, 已存檔：{EMB_FILES[mode]}, {FAISS_FILES[mode]}")

    print("\n✅ 全部完成：faiss1/2/3/4.index 皆已建立")
