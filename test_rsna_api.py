"""
Test RSNA RadReport API directly to diagnose the issue
"""

import requests
import json

print("=" * 80)
print("RSNA API DIAGNOSTIC TEST")
print("=" * 80)
print()

# Test 1: Check API availability
print("Test 1: Check API Availability")
print("-" * 80)

base_url = "https://api3.rsna.org/radreport/v1"
templates_url = f"{base_url}/templates"

try:
    print(f"Testing URL: {templates_url}")
    response = requests.get(
        templates_url, params={"search": "Chest", "limit": 5}, timeout=10
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print()

    if response.status_code == 200:
        print("✅ API is accessible")
        data = response.json()
        print(f"Response structure: {list(data.keys())}")

        if "DATA" in data:
            results = data["DATA"]
            print(f"Number of results: {len(results)}")

            if len(results) > 0:
                print("\nFirst result:")
                print(json.dumps(results[0], indent=2))
            else:
                print("⚠️ No results returned")
        else:
            print("⚠️ No 'DATA' key in response")
            print(f"Raw response: {json.dumps(data, indent=2)[:500]}...")
    else:
        print(f"❌ API returned error: {response.status_code}")
        print(f"Error message: {response.text[:500]}")

except requests.exceptions.ConnectionError as e:
    print(f"❌ Connection Error: {e}")
    print("The API server might be down or inaccessible")
except requests.exceptions.Timeout as e:
    print(f"❌ Timeout Error: {e}")
    print("The API is taking too long to respond")
except Exception as e:
    print(f"❌ Unexpected Error: {type(e).__name__}: {e}")

print()
print("=" * 80)

# Test 2: Check different endpoints
print("\nTest 2: Trying alternate API paths")
print("-" * 80)

alternate_urls = [
    "https://api3.rsna.org/radreport/v1/templates",
    "https://api.rsna.org/radreport/v1/templates",
    "https://radreport.org/api/v1/templates",
]

for url in alternate_urls:
    try:
        print(f"\nTrying: {url}")
        response = requests.get(url, timeout=5)
        print(f"  Status: {response.status_code}")
        if response.status_code == 200:
            print(f"  ✅ This URL works!")
            break
    except:
        print(f"  ❌ Failed")

print()
print("=" * 80)
print("RECOMMENDATION:")
print("=" * 80)

print("""
If all endpoints fail:
1. The RSNA API might be temporarily down
2. The API structure may have changed
3. CORS or authentication might be required

Solutions:
1. Use local template database instead of API
2. Cache templates from successful API calls
3. Implement fallback to hardcoded templates
""")
