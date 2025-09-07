
import json
import pandas as pd

INPUT_FILE = "raw_financial.csv"   # e.g., CSV with columns [question, answer]
OUTPUT_FILE = "financial_data.json"

df = pd.read_csv(INPUT_FILE)

records = []
for _, row in df.iterrows():
    records.append({
        "instruction": row["question"],
        "input": "",
        "output": row["answer"]
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Saved {len(records)} samples to {OUTPUT_FILE}")
