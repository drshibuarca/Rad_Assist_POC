import json
import os

vocab_path = r"c:\Users\Dr Shibu\OneDrive\Desktop\Git hub\Rad_Assist\Radiology Assistant\backend\data\medical_vocab_5000_plus.json"

new_findings = [
    "pneumothorax",
    "effusion",
    "mass",
    "nodule",
    "opacity",
    "consolidation",
    "atelectasis",
    "spiculated",
    "lesion",
    "thickening",
    "edema",
    "fracture",
    "hemorrhage",
    "infarction",
    "stenosis",
    "aneurysm",
    "thrombosis",
    "embolism",
    "calcification",
    "cyst",
    "metastasis",
    "tumor",
    "abscess",
    "infection",
    "inflammation",
]

new_anatomy = ["mediastinal", "pleural", "hilar", "parenchymal", "osseous", "vascular"]


def create_term_entry(term, category):
    return {
        "term": term,
        "abbreviation": None,
        "variants": [],
        "phonetic_similar": [],
        "snomed_code": None,
        "category": category,
    }


with open(vocab_path, "r") as f:
    data = json.load(f)

# Add findings
existing_findings = {item["term"].lower() for item in data["findings"]}
count_added = 0
for term in new_findings:
    if term.lower() not in existing_findings:
        data["findings"].append(create_term_entry(term, "finding"))
        existing_findings.add(term.lower())
        count_added += 1
        print(f"Added finding: {term}")

# Add anatomy
existing_anatomy = {item["term"].lower() for item in data["anatomy"]}
for term in new_anatomy:
    if term.lower() not in existing_anatomy:
        data["anatomy"].append(create_term_entry(term, "anatomy"))
        existing_anatomy.add(term.lower())
        count_added += 1
        print(f"Added anatomy: {term}")

print(f"Total terms added: {count_added}")

with open(vocab_path, "w") as f:
    json.dump(data, f, indent=2)
