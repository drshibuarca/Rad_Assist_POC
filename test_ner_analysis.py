<<<<<<< HEAD
import requests
import json
import time

def test_analysis():
    url = "http://localhost:8000/analysis/ner"
    text = "Patient has a 5mm nodule in the right upper lobe. No pleural effusion. History of pneumonia."
    
    print(f"Testing NER Analysis Endpoint: {url}")
    print(f"Input Text: {text}")
    
    try:
        start_time = time.time()
        response = requests.post(url, json={"text": text})
        end_time = time.time()
        
        print(f"Status: {response.status_code}")
        print(f"Latency: {end_time - start_time:.4f}s")
        
        if response.status_code == 200:
            print("Response:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error Response: {response.text}")
            
    except Exception as e:
        print(f"Connection Error: {e}")
        print("Ensure backend is running on port 8000.")

if __name__ == "__main__":
    test_analysis()
=======
import requests
import json
import time

def test_analysis():
    url = "http://localhost:8000/analysis/ner"
    text = "Patient has a 5mm nodule in the right upper lobe. No pleural effusion. History of pneumonia."
    
    print(f"Testing NER Analysis Endpoint: {url}")
    print(f"Input Text: {text}")
    
    try:
        start_time = time.time()
        response = requests.post(url, json={"text": text})
        end_time = time.time()
        
        print(f"Status: {response.status_code}")
        print(f"Latency: {end_time - start_time:.4f}s")
        
        if response.status_code == 200:
            print("Response:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error Response: {response.text}")
            
    except Exception as e:
        print(f"Connection Error: {e}")
        print("Ensure backend is running on port 8000.")

if __name__ == "__main__":
    test_analysis()
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
