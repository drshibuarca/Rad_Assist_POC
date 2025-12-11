"""
Test script for NER service

Tests entity extraction, assertion/negation detection with sample radiology reports.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.services.ner_service import ner_service


def test_ner():
    """Test NER service with sample reports"""

    print("=" * 60)
    print("NER Service Test")
    print("=" * 60)

    # Initialize service
    print("\nInitializing NER service...")
    ner_service.initialize()

    if not ner_service.is_ready:
        print("❌ NER Service failed to initialize")
        return

    print(f"✓ NER Service initialized")
    print(f"✓ Loaded {len(ner_service.vocab_lookup)} vocabulary terms")

    # Test cases
    test_reports = [
        {
            "name": "Normal Chest X-Ray",
            "text": "The lungs are clear. No pleural effusion or pneumothorax. Heart size is normal.",
        },
        {
            "name": "Abnormal Chest CT",
            "text": "There is a 5mm nodule in the right upper lobe. Consolidation present in the left lower lobe. No pleural effusion.",
        },
        {
            "name": "Complex Finding",
            "text": "Atelectasis is noted in the RLL. Ground glass opacity demonstrates in bilateral lung fields. The pleura is unremarkable.",
        },
    ]

    for test in test_reports:
        print(f"\n" + "-" * 60)
        print(f"Test: {test['name']}")
        print(f"Text: {test['text']}")
        print("-" * 60)

        result = ner_service.analyze(test["text"])

        if "error" in result:
            print(f"❌ Error: {result['error']}")
            continue

        print(f"\n✓ Found {result['entity_count']} entities:\n")

        for entity in result["entities"]:
            label_icon = {
                "ANATOMY": "🫁",
                "FINDINGS": "📋",
                "MEASUREMENTS": "📏",
                "ASSERTION": "✓",
                "NEGATION": "✗",
            }.get(entity["label"], "•")

            negation_marker = " [NEGATED]" if entity.get("negated") else ""
            assertion_marker = " [ASSERTED]" if entity.get("asserted") else ""
            confidence = (
                f" ({entity.get('confidence', 0):.2f})"
                if "confidence" in entity
                else ""
            )

            print(
                f"{label_icon} {entity['label']:15} | {entity['text']:30} | Pos: {entity['start']}-{entity['end']}{negation_marker}{assertion_marker}{confidence}"
            )

            if entity.get("snomed_code"):
                print(f"   └─ SNOMED: {entity['snomed_code']}")


if __name__ == "__main__":
    test_ner()
