<<<<<<< HEAD
import requests
import json

BASE_URL = "https://api3.rsna.org/radreport/v1"

def test_search():
    print("Searching for 'Chest' templates...")
    url = f"{BASE_URL}/templates"
    params = {
        "search": "Chest",
        "limit": 5
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get('DATA', [])
        print(f"Found {len(results)} templates.")
        
        if results:
            first_template = results[0]
            t_id = first_template['template_id']
            print(f"First Template: {first_template['title']} (ID: {t_id})")
            return t_id
    except Exception as e:
        print(f"Search Error: {e}")
        return None

def test_details(template_id):
    print(f"\nFetching details for Template ID: {template_id}...")
    url = f"{BASE_URL}/templates/{template_id}/details"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        template_data = data.get('DATA', {})
        inner_data = template_data.get('templateData')
        print("TemplateData Type:", type(inner_data))
        print("TemplateData Snippet:", str(inner_data)[:500])
    except Exception as e:
        print(f"Details Error: {e}")

if __name__ == "__main__":
    t_id = test_search()
    if t_id:
        test_details(t_id)
=======
import requests
import json

BASE_URL = "https://api3.rsna.org/radreport/v1"

def test_search():
    print("Searching for 'Chest' templates...")
    url = f"{BASE_URL}/templates"
    params = {
        "search": "Chest",
        "limit": 5
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get('DATA', [])
        print(f"Found {len(results)} templates.")
        
        if results:
            first_template = results[0]
            t_id = first_template['template_id']
            print(f"First Template: {first_template['title']} (ID: {t_id})")
            return t_id
    except Exception as e:
        print(f"Search Error: {e}")
        return None

def test_details(template_id):
    print(f"\nFetching details for Template ID: {template_id}...")
    url = f"{BASE_URL}/templates/{template_id}/details"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        template_data = data.get('DATA', {})
        inner_data = template_data.get('templateData')
        print("TemplateData Type:", type(inner_data))
        print("TemplateData Snippet:", str(inner_data)[:500])
    except Exception as e:
        print(f"Details Error: {e}")

if __name__ == "__main__":
    t_id = test_search()
    if t_id:
        test_details(t_id)
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
