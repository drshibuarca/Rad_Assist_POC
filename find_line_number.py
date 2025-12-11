import os

vocab_path = os.path.join("backend", "data", "medical_vocab_5000_plus.json")

with open(vocab_path, "r") as f:
    for i, line in enumerate(f):
        if '"findings": [' in line:
            print(f"Found 'findings' at line {i + 1}")
            break
        if '"measurements": [' in line:
            print(f"Found 'measurements' at line {i + 1}")
