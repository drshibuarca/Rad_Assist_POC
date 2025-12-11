import requests
import json

# Test the generate_report endpoint with a report containing pneumothorax
url = "http://localhost:8000/generate_report"

payload = {
    "modality": "CT Chest",
    "transcript": "There is left-sided pneumothorax measuring 3 cm",
    "custom_template": None,
}

print("Testing /generate_report endpoint...")
print(f"Request: {json.dumps(payload, indent=2)}")
print("\n" + "=" * 80 + "\n")

try:
    response = requests.post(url, json=payload, timeout=30)
    print(f"Status Code: {response.status_code}\n")

    if response.status_code == 200:
        data = response.json()
        print("Response Keys:", list(data.keys()))
        print("\n" + "-" * 80)
        print("\nReport Preview:")
        print(data.get("report", "N/A")[:500])
        print("\n" + "-" * 80)

        if "critical_findings" in data:
            cf = data["critical_findings"]
            print("\nCRITICAL FINDINGS:")
            print(f"  has_critical_findings: {cf.get('has_critical_findings')}")
            print(f"  total_count: {cf.get('total_count')}")

            if cf.get("all_findings"):
                print(f"\n  All Findings ({len(cf['all_findings'])}):")
                for finding in cf["all_findings"]:
                    print(f"\n    - Type: {finding.get('type')}")
                    print(f"      Urgency: {finding.get('urgency')}")
                    print(f"      Message: {finding.get('message')}")
                    print(f"      Confidence: {finding.get('confidence')}")
                    print(f"      Matched Text: {finding.get('matched_text')}")
            else:
                print("\n  No findings in all_findings array")
        else:
            print("\n❌ No 'critical_findings' in response!")
            print("\nFull Response:")
            print(json.dumps(data, indent=2))
    else:
        print(f"❌ Error: {response.text}")

except Exception as e:
    print(f"❌ Exception: {e}")
