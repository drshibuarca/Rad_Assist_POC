import asyncio
from backend.services.correction_service import correction_service


async def test_correction_robustness():
    # Test cases that might have failed with higher threshold
    test_cases = [
        ("pneumothrax", "pneumothorax"),  # Missing 'o'
        ("numothorax", "pneumothorax"),  # Phonetic start
        ("abdoman", "abdomen"),  # Vowel swap
        ("hemorage", "hemorrhage"),  # Missing letters
        ("skelital", "skeletal"),  # Vowel swap
    ]

    print("\n---------------------------------------------------")
    print("Testing Correction Engine Robustness (Threshold: 0.80)")
    print("---------------------------------------------------")

    passed = 0
    for typo, expected in test_cases:
        result = await correction_service.correct_transcription(typo)
        corrected = result["text"]

        match_info = result["words"][0]
        confidence = match_info.get("confidence", 0)

        if corrected.lower() == expected.lower():
            print(f"✅ '{typo}' -> '{corrected}' (Conf: {confidence:.2f})")
            passed += 1
        else:
            print(f"❌ '{typo}' -> '{corrected}' (Expected: '{expected}')")

    print("---------------------------------------------------")
    print(f"Passed: {passed}/{len(test_cases)}")

    if passed >= 4:
        print("TEST PASSED: Correction engine is robust.")
    else:
        print("TEST FAILED: Correction engine missed too many typos.")
        exit(1)


if __name__ == "__main__":
    asyncio.run(test_correction_robustness())
