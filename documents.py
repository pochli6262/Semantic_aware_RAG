import os
import json
import difflib
from openai import OpenAI
from tqdm import tqdm

client = OpenAI()

base_path = "Code_python"
doc_file = "documents.jsonl"

# 先收集有 fault/correct 的目錄
folders = []
for root, dirs, files in os.walk(base_path):
    if "faultyVersion.py" in files and "correctVersion.py" in files:
        folders.append(root)

with open(doc_file, "w", encoding="utf-8") as f_out:
    for root in tqdm(folders, desc="Stage 1: Building documents"):
        doc_id = os.path.basename(root)

        with open(os.path.join(root, "faultyVersion.py")) as f:
            buggy = f.read()
        with open(os.path.join(root, "correctVersion.py")) as f:
            correct = f.read()

        # 產生 diff
        diff = "\n".join(
            difflib.unified_diff(
                buggy.splitlines(),
                correct.splitlines(),
                lineterm=""
            )
        )

        # GPT 生成錯誤描述
        try:
            problem = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a program analysis assistant. Describe the problem in the buggy code in one concise English sentence."},
                    {"role": "user", "content": f"Buggy code:\n{buggy}\nCorrect code:\n{correct}"}
                ]
            ).choices[0].message.content
        except Exception as e:
            problem = f"[Error generating problem: {e}]"

        # 建立 document
        doc = {
            "id": doc_id,
            "problem": problem,
            "buggy_code": buggy,
            "diff": diff
        }

        # 寫入 JSONL
        f_out.write(json.dumps(doc, ensure_ascii=False) + "\n")

print(f"完成 ✅ 已存成 {doc_file}")
