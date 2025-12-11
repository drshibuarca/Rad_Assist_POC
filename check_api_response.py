<<<<<<< HEAD
import requests
import json

try:
    response = requests.get("http://127.0.0.1:8001/radreport/search?query=Chest")
    response.raise_for_status()
    data = response.json()
    if data:
        print(f"Found {len(data)} results:")
        for item in data:
            print(f"- {item.get('title')} ({item.get('lang')})")
    else:
        print("No results found")
except Exception as e:
    print(f"Error: {e}")
=======
import requests
import json

try:
    response = requests.get("http://127.0.0.1:8001/radreport/search?query=Chest")
    response.raise_for_status()
    data = response.json()
    if data:
        print(f"Found {len(data)} results:")
        for item in data:
            print(f"- {item.get('title')} ({item.get('lang')})")
    else:
        print("No results found")
except Exception as e:
    print(f"Error: {e}")
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
