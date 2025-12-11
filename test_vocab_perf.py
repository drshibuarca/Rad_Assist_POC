<<<<<<< HEAD
import time
import sys
import os
import asyncio

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.services.correction_service import correction_service

async def test_performance():
    print("=" * 60)
    print("Vocabulary Performance Test")
    print("=" * 60)
    
    # Measure load time (already loaded on import, but we can check list size)
    print(f"Vocabulary Size: {len(correction_service.all_terms)} terms")
    
    # Test correction speed
    test_phrase = "patient has pneomonia in the right upper lobule and atelectasis"
    print(f"\nTest Phrase: '{test_phrase}'")
    
    start_time = time.time()
    result = await correction_service.correct_transcription(test_phrase)
    end_time = time.time()
    
    duration_ms = (end_time - start_time) * 1000
    print(f"Correction took: {duration_ms:.2f} ms")
    
    print("\nCorrected Text:")
    print(result["text"])
    
    print("\nCorrections:")
    for word in result["words"]:
        if word.get("corrected"):
            print(f"  - '{word['original']}' -> '{word['word']}' (Conf: {word['confidence']:.2f})")
            if "sctid" in word:
                print(f"    SNOMED: {word['snomed_term']} ({word['sctid']})")

    if duration_ms < 100:
        print("\n✓ Performance: EXCELLENT (<100ms)")
    elif duration_ms < 500:
        print("\n✓ Performance: GOOD (<500ms)")
    else:
        print("\n⚠️ Performance: SLOW (>500ms)")

if __name__ == "__main__":
    asyncio.run(test_performance())
=======
import time
import sys
import os
import asyncio

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.services.correction_service import correction_service

async def test_performance():
    print("=" * 60)
    print("Vocabulary Performance Test")
    print("=" * 60)
    
    # Measure load time (already loaded on import, but we can check list size)
    print(f"Vocabulary Size: {len(correction_service.all_terms)} terms")
    
    # Test correction speed
    test_phrase = "patient has pneomonia in the right upper lobule and atelectasis"
    print(f"\nTest Phrase: '{test_phrase}'")
    
    start_time = time.time()
    result = await correction_service.correct_transcription(test_phrase)
    end_time = time.time()
    
    duration_ms = (end_time - start_time) * 1000
    print(f"Correction took: {duration_ms:.2f} ms")
    
    print("\nCorrected Text:")
    print(result["text"])
    
    print("\nCorrections:")
    for word in result["words"]:
        if word.get("corrected"):
            print(f"  - '{word['original']}' -> '{word['word']}' (Conf: {word['confidence']:.2f})")
            if "sctid" in word:
                print(f"    SNOMED: {word['snomed_term']} ({word['sctid']})")

    if duration_ms < 100:
        print("\n✓ Performance: EXCELLENT (<100ms)")
    elif duration_ms < 500:
        print("\n✓ Performance: GOOD (<500ms)")
    else:
        print("\n⚠️ Performance: SLOW (>500ms)")

if __name__ == "__main__":
    asyncio.run(test_performance())
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
