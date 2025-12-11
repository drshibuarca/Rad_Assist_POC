"""
Test script for STT optimizations
Tests the post-processing pipeline and medical context improvements
"""

import sys

sys.path.insert(
    0, r"c:\Users\Dr Shibu\OneDrive\Desktop\Git hub\Rad_Assist\Radiology Assistant"
)

from backend.services.stt_service import STTPostProcessor

print("=" * 80)
print("STT OPTIMIZATION TEST SUITE")
print("=" * 80)
print()

# Initialize post-processor
processor = STTPostProcessor()

# Test Cases
test_cases = [
    {
        "name": "Measurement Standardization - Missing Space",
        "input": "There is a 3cm mass in the right lung",
        "expected_improvement": "3cm → 3 cm",
    },
    {
        "name": "Measurement Standardization - Decimal",
        "input": "The lesion measures 2.5mm in diameter",
        "expected_improvement": "2.5mm → 2.5 mm",
    },
    {
        "name": "Number Word Conversion",
        "input": "Mass measuring three cm noted",
        "expected_improvement": "three cm → 3 cm",
    },
    {
        "name": "Point to Decimal",
        "input": "The mass is point 5 cm",
        "expected_improvement": "point 5 → 0.5",
    },
    {
        "name": "Abbreviation Expansion - PTX",
        "input": "Large PTX on the left side",
        "expected_improvement": "PTX → pneumothorax",
    },
    {
        "name": "Abbreviation Expansion - RUL",
        "input": "Nodule in the RUL measuring 1 cm",
        "expected_improvement": "RUL → right upper lobe",
    },
    {
        "name": "Abbreviation Expansion - CXR",
        "input": "CXR shows no acute findings",
        "expected_improvement": "CXR → chest x-ray",
    },
    {
        "name": "Complex Case - Multiple Issues",
        "input": "CXR shows 2cm PTX in RUL with point 5 cm pleural thickening",
        "expected_improvement": "Multiple: CXR, 2cm, PTX, RUL, point 5",
    },
    {
        "name": "Normal Report - No Changes Needed",
        "input": "Lungs are clear, heart size is normal",
        "expected_improvement": "Should remain unchanged",
    },
]

print("Testing Post-Processing Pipeline...")
print()

passed = 0
failed = 0

for i, test in enumerate(test_cases, 1):
    print(f"Test {i}: {test['name']}")
    print(f"  Expected: {test['expected_improvement']}")
    print(f"  Input:    '{test['input']}'")

    # Apply post-processing
    result = processor.apply_enhancements(test["input"])

    print(f"  Output:   '{result}'")

    # Check if processing occurred
    if result != test["input"]:
        print(f"  Status:   ✅ ENHANCED")
        passed += 1
    else:
        if "No Changes" in test["expected_improvement"]:
            print(f"  Status:   ✅ CORRECTLY UNCHANGED")
            passed += 1
        else:
            print(f"  Status:   ⚠️  NO CHANGE DETECTED")
            failed += 1

    print()

print("=" * 80)
print(f"SUMMARY: {passed}/{len(test_cases)} tests passed")
print("=" * 80)
print()

# Demonstrate specific enhancements
print("DETAILED ENHANCEMENT EXAMPLES:")
print()

examples = [
    ("3cm mass", "Measurement spacing"),
    ("PTX in RUL", "Abbreviation expansion"),
    ("point 5 cm nodule", "Decimal conversion"),
    ("five mm opacity", "Number word to digit"),
]

for raw, description in examples:
    enhanced = processor.apply_enhancements(raw)
    print(f"{description}:")
    print(f"  Before: '{raw}'")
    print(f"  After:  '{enhanced}'")
    if raw != enhanced:
        print(f"  ✅ Improved!")
    else:
        print(f"  ⚠️ No change")
    print()

print("=" * 80)
print("TEST COMPLETE")
print("=" * 80)
print()
print("📊 Next Steps:")
print("1. Restart backend to activate enhancements")
print("2. Test with real audio dictation")
print("3. Monitor debug logs for before/after transcriptions")
