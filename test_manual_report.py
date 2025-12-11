import requests
import json

URL = "http://localhost:8000/generate_report"

payload = {
    "modality": "CT Chest",
    "transcript": "Patient is a 45 year old male. The lungs are clear. No pleural effusion. The heart size is normal. No mediastinal mass. The bones are unremarkable.",
    "custom_template": """
    FINDINGS:
    Lungs: (Standard Normal: Clear.)
    Pleura: (Standard Normal: No effusion.)
    Heart: (Standard Normal: Normal size.)
    Mediastinum: (Standard Normal: No mass.)
    Bones: (Standard Normal: Intact.)
    
    IMPRESSION:
    """
}

try:
    response = requests.post(URL, json=payload)
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Response JSON:", json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, 'response') and e.response:
        print("Response Text:", e.response.text)
