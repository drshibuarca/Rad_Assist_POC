import json
import os

vocab_path = os.path.join("backend", "data", "medical_vocab_5000_plus.json")

try:
    with open(vocab_path, "r") as f:
        data = json.load(f)

    print(f"Loaded vocab from {vocab_path}")

    terms_to_check = ["pneumothorax", "abdomen", "skeletal", "hemorrhage"]

    for term_to_check in terms_to_check:
        found = False
        for category in ["findings", "anatomy", "measurements"]:
            for item in data.get(category, []):
                if item["term"].lower() == term_to_check:
                    print(f"Found '{term_to_check}' in {category}")
                    found = True
                    break
            if found:
                break

        if not found:
            print(f"'{term_to_check}' NOT found in vocabulary")

except Exception as e:
    print(f"Error: {e}")
