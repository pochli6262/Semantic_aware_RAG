import os
import json
import openai

# 設定 OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE")

CODE_NEW = "Code_new"
OUTPUT_JSON = "oracle_summaries.json"

# 載入已存在的 summaries
if os.path.exists(OUTPUT_JSON):
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        oracle_summaries = json.load(f)
else:
    oracle_summaries = {}

def generate_summary(buggy_code, correct_code):
    """呼叫 GPT 產生 oracle summary"""
    prompt = f"""
You are a Python repair analysis assistant.

Buggy Program:
{buggy_code}

Correct Program:
{correct_code}

Task:
Summarize the root cause of the bug in one concise sentence.
"""
    resp = openai.chat.completions.create(
        model="gpt-5-mini",  # 可以改成 gpt-4o-mini
        messages=[{"role": "user", "content": prompt}],
    )

    return resp.choices[0].message.content.strip()

# --- 遍歷 Code_new ---
for problem in os.listdir(CODE_NEW):
    problem_path = os.path.join(CODE_NEW, problem)
    if not os.path.isdir(problem_path):
        continue

    lang_path = os.path.join(problem_path, "Python")
    if not os.path.isdir(lang_path):
        continue

    for submission in os.listdir(lang_path):
        submission_path = os.path.join(lang_path, submission)
        if not os.path.isdir(submission_path):
            continue

        task_key = f"{problem}/Python/{submission}"
        if task_key in oracle_summaries:
            print(f"⏩ Skip {task_key}, already summarized.")
            continue

        buggy_file = os.path.join(submission_path, "faultyVersion.py")
        correct_file = os.path.join(submission_path, "correctVersion.py")

        if not os.path.exists(buggy_file) or not os.path.exists(correct_file):
            print(f"⚠️ Missing files for {task_key}, skip.")
            continue

        with open(buggy_file, "r", encoding="utf-8") as f:
            buggy_code = f.read()
        with open(correct_file, "r", encoding="utf-8") as f:
            correct_code = f.read()

        print(f"🔎 Generating summary for {task_key} ...")
        summary = generate_summary(buggy_code, correct_code)

        oracle_summaries[task_key] = summary

        # 每次寫回，避免中途掛掉丟失進度
        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(oracle_summaries, f, indent=2, ensure_ascii=False)

print("🎯 All done! Summaries stored in", OUTPUT_JSON)
