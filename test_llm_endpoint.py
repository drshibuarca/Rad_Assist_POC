<<<<<<< HEAD
import requests
import json

url = "http://localhost:8001/generate_report"
payload = {
    "modality": "CXR (Chest X-Ray)",
    "transcript": "Patient has a 5mm nodule in the right upper lobe."
}

try:
    print(f"Sending request to {url}...")
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("\n--- Generated Report ---\n")
        print(data.get("report"))
        print("\n------------------------\n")
    else:
        print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
=======
import requests
import json

url = "http://localhost:8001/generate_report"
payload = {
    "modality": "CXR (Chest X-Ray)",
    "transcript": "Patient has a 5mm nodule in the right upper lobe."
}

try:
    print(f"Sending request to {url}...")
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("\n--- Generated Report ---\n")
        print(data.get("report"))
        print("\n------------------------\n")
    else:
        print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
