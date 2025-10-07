#!/usr/bin/env python3
import os
import json
import re
import openai

# ====== 設定 ======
API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE") 
SOURCE_DIR = "Code_new"   # 原始程式碼資料夾
PROBLEM_DIR = "problems"  # 題目描述資料夾 (每題一個資料夾，內有 statement.md)

MODEL_ID = "gpt-5-mini"

OUTPUT_DIR = f"repaired_programs_{MODEL_ID}_stage2"
RAW_OUTPUT_DIR = f"raw_outputs_{MODEL_ID}_stage2"
FAILED_LOG = f"failed_files_{MODEL_ID}_stage2.txt"
MAX_RETRIES = 3

# 初始化 API
openai.api_key = API_KEY

# 建立資料夾
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RAW_OUTPUT_DIR, exist_ok=True)

# ====== 工具函數 ======

def build_prompt(code: str, description: str) -> str:
    return f"""
You are a Python expert.

A user gives you the following Python function which is buggy.

## Problem Description:
{description}

## Buggy Code:
{code}

Your task:
1. Identify the bug.
2. Assume the bug is caused by ONLY ONE LINE being incorrect.
3. Provide the corrected version of the ENTIRE program,
   but change only that single line — all other lines must remain identical.
4. Do not restructure or rewrite unrelated code.
5. Respond ONLY in JSON format:

{{
  "explanation": "Explain what was wrong in that single line and how you fixed it.",
  "fixed_code": "The FULL Program with only that line corrected. Do not just return one line. Return the ENTIRE program."
}}
""".strip()


def extract_json_best_effort(raw: str):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                return None
    return None


def repair_file(file_path: str, desc_path: str, out_json_path: str, out_py_path: str):
    """修復單一檔案（含 retry 機制）"""
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    description = ""
    if os.path.exists(desc_path):
        with open(desc_path, "r", encoding="utf-8") as f:
            description = f.read().strip()

    prompt = build_prompt(code, description)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = openai.chat.completions.create(
                model=MODEL_ID,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response.choices[0].message.content

            # 儲存 GPT 原始輸出
            raw_path = os.path.join(
                RAW_OUTPUT_DIR,
                os.path.basename(out_json_path).replace(".json", f"_try{attempt}.txt")
            )
            with open(raw_path, "w", encoding="utf-8") as fout:
                fout.write(content)

            # 嘗試解析 JSON
            result = extract_json_best_effort(content)
            if result and "fixed_code" in result:
                os.makedirs(os.path.dirname(out_json_path), exist_ok=True)
                with open(out_json_path, "w", encoding="utf-8") as out:
                    json.dump(result, out, ensure_ascii=False, indent=2)
                with open(out_py_path, "w", encoding="utf-8") as fpy:
                    fpy.write(result["fixed_code"])
                print(f"✅ 修復完成：{os.path.basename(file_path)}")
                return
            else:
                print(f"⚠️ 第 {attempt} 次 JSON 解析失敗：{os.path.basename(file_path)}")
        except Exception as e:
            print(f"🔥 第 {attempt} 次 API 錯誤：{file_path}: {e}")

    # 三次都失敗
    with open(FAILED_LOG, "a", encoding="utf-8") as flog:
        flog.write(file_path + "\n")
    print(f"❌ 放棄修復：{os.path.basename(file_path)}，已記錄到 {FAILED_LOG}")


# ====== 主流程 ======
if __name__ == "__main__":
    for dirpath, _, filenames in os.walk(SOURCE_DIR):
        for filename in filenames:
            if filename == "faultyVersion.py":
                src_path = os.path.join(dirpath, filename)

                # 取得題目名稱（假設 Code_new/abc221_f/faultyVersion.py → abc221_f）
                problem_name = os.path.basename(dirpath)
                desc_path = os.path.join(PROBLEM_DIR, problem_name, "statement.md")

                # 輸出路徑
                rel_path = os.path.relpath(dirpath, SOURCE_DIR)
                base_name = filename.replace(".py", "")
                out_json_path = os.path.join(OUTPUT_DIR, rel_path, base_name + ".json")
                out_py_path = os.path.join(OUTPUT_DIR, rel_path, base_name + ".py")

                repair_file(src_path, desc_path, out_json_path, out_py_path)
