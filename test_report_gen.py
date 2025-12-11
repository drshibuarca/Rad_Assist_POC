<<<<<<< HEAD
import requests
import json

def test_report_generation():
    url = "http://localhost:8000/generate_report"
    
    payload = {
        "modality": "chest_xray",
        "transcript": "Patient is a 45 year old male with cough. Lungs are clear. Heart size is normal. No pleural effusion or pneumothorax. Bones are unremarkable."
    }
    
    print("Testing Report Generation with Gemini...")
    print(f"URL: {url}")
    print(f"Transcript: {payload['transcript']}")
    print("-" * 50)
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            print("SUCCESS!")
            print("Generated Report:")
            print("-" * 50)
            print(result.get("report", "No report found"))
            print("-" * 50)
        else:
            print(f"FAILED. Status Code: {response.status_code}")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_report_generation()
=======
import requests
import json

def test_report_generation():
    url = "http://localhost:8000/generate_report"
    
    payload = {
        "modality": "chest_xray",
        "transcript": "Patient is a 45 year old male with cough. Lungs are clear. Heart size is normal. No pleural effusion or pneumothorax. Bones are unremarkable."
    }
    
    print("Testing Report Generation with Gemini...")
    print(f"URL: {url}")
    print(f"Transcript: {payload['transcript']}")
    print("-" * 50)
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            print("SUCCESS!")
            print("Generated Report:")
            print("-" * 50)
            print(result.get("report", "No report found"))
            print("-" * 50)
        else:
            print(f"FAILED. Status Code: {response.status_code}")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_report_generation()
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
