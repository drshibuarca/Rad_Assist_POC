<<<<<<< HEAD
import requests
import json

url = "http://localhost:8001/radreport/search?query=Chest&limit=3"

try:
    print(f"Sending request to {url}...")
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Found {len(data)} templates.")
        if data:
            print(f"First: {data[0]['title']} (ID: {data[0]['template_id']})")
    else:
        print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
=======
import requests
import json

url = "http://localhost:8001/radreport/search?query=Chest&limit=3"

try:
    print(f"Sending request to {url}...")
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Found {len(data)} templates.")
        if data:
            print(f"First: {data[0]['title']} (ID: {data[0]['template_id']})")
    else:
        print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
