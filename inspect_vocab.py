import json

with open(
    r"c:\Users\Dr Shibu\OneDrive\Desktop\Git hub\Rad_Assist\Radiology Assistant\backend\data\medical_vocab_5000_plus.json",
    "r",
) as f:
    data = json.load(f)
    print("Keys:", data.keys())
    if "findings" in data:
        print("Findings count:", len(data["findings"]))
    else:
        print("Findings key NOT found")
