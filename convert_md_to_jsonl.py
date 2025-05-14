import sys
import json
import re

if len(sys.argv) < 2:
    print("Usage: python convert_md_to_jsonl.py input.md [output.jsonl]")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2] if len(sys.argv) > 2 else "output.jsonl"

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

rows = []
header_found = False

for line in lines:
    if not header_found:
        if re.match(r"^\|[- ]+\|[- ]+\|[- ]+\|", line):
            header_found = True
        continue
    if not line.strip().startswith("|"):
        continue
    parts = [p.strip() for p in line.strip().split("|")[1:-1]]
    if len(parts) < 3:
        continue
    prompt = parts[1]
    content = parts[2]
    rows.append({
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": content}
        ]
    })

with open(output_path, "w", encoding="utf-8") as out:
    for row in rows:
        out.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"✅ JSONL file created: {output_path}")
