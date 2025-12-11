import asyncio
from backend.services.critical_findings import critical_findings_detector


async def test_critical_findings():
    """Test the critical findings detector with sample reports"""

    # Test Case 1: Pneumothorax
    test_report_1 = """
    CT CHEST WITHOUT CONTRAST
    
    FINDINGS:
    There is a large right-sided pneumothorax measuring approximately 3 cm.
    The mediastinum is shifted toward the left.
    No pleural effusion.
    
    IMPRESSION:
    1. Large right pneumothorax with mediastinal shift, concerning for tension physiology.
    2. Recommend immediate clinical correlation.
    """

    # Test Case 2: Pulmonary Embolism
    test_report_2 = """
    CT PULMONARY ANGIOGRAM
    
    FINDINGS:
    There is a large filling defect in the right main pulmonary artery consistent with 
    acute pulmonary embolism. Additional smaller emboli are seen in segmental branches.
    
    IMPRESSION:
    1. Acute pulmonary embolism involving right main and segmental pulmonary arteries.
    """

    # Test Case 3: Intracranial Hemorrhage
    test_report_3 = """
    CT HEAD WITHOUT CONTRAST
    
    FINDINGS:
    There is an acute subdural hematoma along the left cerebral convexity measuring 
    8mm in maximum thickness. There is 5mm of rightward midline shift.
    
    IMPRESSION:
    1. Acute subdural hematoma with mass effect and midline shift.
    2. Immediate neurosurgical consultation recommended.
    """

    # Test Case 4: Normal Report (No Critical Findings)
    test_report_4 = """
    CHEST X-RAY
    
    FINDINGS:
    The lungs are clear bilaterally. No pneumothorax or pleural effusion.
    The cardiac silhouette is normal in size.
    
    IMPRESSION:
    1. Normal chest x-ray.
    """

    test_cases = [
        ("Pneumothorax", test_report_1),
        ("Pulmonary Embolism", test_report_2),
        ("Intracranial Hemorrhage", test_report_3),
        ("Normal Report", test_report_4),
    ]

    print("=" * 80)
    print("CRITICAL FINDINGS DETECTION TEST")
    print("=" * 80)

    for test_name, report_text in test_cases:
        print(f"\n\n{'=' * 80}")
        print(f"TEST: {test_name}")
        print(f"{'=' * 80}")
        print(f"\nReport Text:\n{report_text}")
        print(f"\n{'-' * 80}")

        # Analyze the report
        results = critical_findings_detector.analyze_report(report_text)

        print(f"\nRESULTS:")
        print(f"  Has Critical Findings: {results['has_critical_findings']}")
        print(f"  Total Count: {results['total_count']}")

        if results["has_critical_findings"]:
            print(f"\n  Findings by Urgency:")

            for urgency in ["stat", "urgent", "important"]:
                findings = results["findings_by_urgency"].get(urgency, [])
                if findings:
                    print(f"\n    {urgency.upper()} ({len(findings)}):")
                    for finding in findings:
                        print(f"      • {finding['message']}")
                        print(f"        Type: {finding['type']}")
                        print(f"        Confidence: {finding['confidence']}")
                        print(f"        Matched Text: '{finding['matched_text']}'")
                        print(f"        Action: {finding['action']}")
                        if finding.get("recommendations"):
                            print(f"        Recommendations:")
                            for rec in finding["recommendations"]:
                                print(f"          - {rec}")
        else:
            print("  ✓ No critical findings detected (as expected)")

    print(f"\n\n{'=' * 80}")
    print("TEST COMPLETE")
    print(f"{'=' * 80}\n")


if __name__ == "__main__":
    asyncio.run(test_critical_findings())
