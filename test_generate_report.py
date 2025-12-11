<<<<<<< HEAD
import requests
import json

url = "http://localhost:8001/generate_report"
payload = {
    "modality": "Test Modality",
    "transcript": "Patient has a 5mm nodule in the right upper lobe.",
    "custom_template": "FINDINGS:\nLungs: (Standard Normal: Clear.)\n\nIMPRESSION:\n"
}

try:
    print(f"Sending request to {url}...")
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    if response.ok:
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print("Error:", response.text)
except Exception as e:
    print(f"Exception: {e}")
=======
import requests
import json

url = "http://localhost:8001/generate_report"
payload = {
    "modality": "Test Modality",
    "transcript": "Patient has a 5mm nodule in the right upper lobe.",
    "custom_template": "FINDINGS:\nLungs: (Standard Normal: Clear.)\n\nIMPRESSION:\n"
}

try:
    print(f"Sending request to {url}...")
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    if response.ok:
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print("Error:", response.text)
except Exception as e:
    print(f"Exception: {e}")
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
