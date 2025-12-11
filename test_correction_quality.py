import asyncio
from backend.services.correction_service import CorrectionService


async def test_correction_quality():
    service = CorrectionService()

    # List of common radiology misspellings -> expected correct term
    test_cases = [
        ("numothorax", "pneumothorax"),
        ("numo", "pneumo"),
        ("atlectasis", "atelectasis"),
        ("effuison", "effusion"),
        ("mediastinal", "mediastinal"),  # Control (correct)
        ("consolidation", "consolidation"),  # Control
        ("masslation", "mass"),  # From user screenshot? "maslation" -> mass/lesion?
        ("speculated", "spiculated"),  # Common error
        ("noduel", "nodule"),
        ("opacit", "opacity"),
        ("skelatal", "skeletal"),
        ("abdoemn", "abdomen"),
    ]

    print(
        f"{'Input':<20} | {'Expected':<20} | {'Result':<20} | {'Score':<10} | {'Status'}"
    )
    print("-" * 90)

    passed = 0
    for wrong, correct in test_cases:
        # We simulate the correction service logic
        # The service takes a full text, but we want to test individual word correction logic
        # We can use phonetic_match directly for this test

        match = service.phonetic_match(wrong)

        result = match[0] if match else "None"
        score = match[1] if match else 0.0

        status = "✅" if result.lower() == correct.lower() else "❌"
        if status == "✅":
            passed += 1

        print(f"{wrong:<20} | {correct:<20} | {result:<20} | {score:<10.2f} | {status}")

        if match and match[2]:
            print(f"  Alternatives: {match[2]}")

    print("-" * 90)
    print(
        f"Accuracy: {passed}/{len(test_cases)} ({passed / len(test_cases) * 100:.1f}%)"
    )


if __name__ == "__main__":
    asyncio.run(test_correction_quality())
