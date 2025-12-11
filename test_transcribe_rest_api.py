<<<<<<< HEAD
import requests
import io
import wave
import struct
import math

def generate_test_audio():
    """Generate a simple sine wave audio file (beep sound) as WAV"""
    sample_rate = 16000
    duration = 2  # seconds
    frequency = 440  # A4 note
    
    # Generate sine wave
    num_samples = int(sample_rate * duration)
    audio_data = []
    
    for i in range(num_samples):
        # Generate sine wave sample
        sample = int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate))
        audio_data.append(sample)
    
    # Create WAV file in memory
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Pack samples as 16-bit integers
        packed_data = struct.pack('<' + 'h' * len(audio_data), *audio_data)
        wav_file.writeframes(packed_data)
    
    wav_buffer.seek(0)
    return wav_buffer

def test_transcribe_endpoint():
    """Test the /transcribe REST API endpoint"""
    url = "http://localhost:8000/transcribe"
    
    print("=" * 60)
    print("Testing /transcribe REST API Endpoint")
    print("=" * 60)
    print(f"URL: {url}")
    print()
    
    try:
        # Generate test audio
        print("Generating test audio file...")
        audio_file = generate_test_audio()
        
        # Prepare request
        files = {'audio': ('test.wav', audio_file, 'audio/wav')}
        
        print("Sending POST request to /transcribe...")
        response = requests.post(url, files=files, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            print("✓ SUCCESS!")
            print()
            print("Response:")
            print(f"  Text: {data.get('text', '(empty)')}")
            print(f"  Word Count: {len(data.get('words', []))}")
            print()
            if data.get('words'):
                print("  First few words:")
                for word_data in data['words'][:5]:
                    print(f"    - {word_data.get('word')}: {word_data.get('confidence', 0):.2f}")
        else:
            print("✗ FAILED!")
            print(f"  Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("✗ CONNECTION ERROR!")
        print("  Backend server is not running on port 8000")
        print("  Please ensure the server is running:")
        print("    backend\\venv311\\Scripts\\python -m uvicorn backend.main:app --reload --port 8000")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    print("=" * 60)

if __name__ == "__main__":
    test_transcribe_endpoint()
=======
import requests
import io
import wave
import struct
import math

def generate_test_audio():
    """Generate a simple sine wave audio file (beep sound) as WAV"""
    sample_rate = 16000
    duration = 2  # seconds
    frequency = 440  # A4 note
    
    # Generate sine wave
    num_samples = int(sample_rate * duration)
    audio_data = []
    
    for i in range(num_samples):
        # Generate sine wave sample
        sample = int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate))
        audio_data.append(sample)
    
    # Create WAV file in memory
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Pack samples as 16-bit integers
        packed_data = struct.pack('<' + 'h' * len(audio_data), *audio_data)
        wav_file.writeframes(packed_data)
    
    wav_buffer.seek(0)
    return wav_buffer

def test_transcribe_endpoint():
    """Test the /transcribe REST API endpoint"""
    url = "http://localhost:8000/transcribe"
    
    print("=" * 60)
    print("Testing /transcribe REST API Endpoint")
    print("=" * 60)
    print(f"URL: {url}")
    print()
    
    try:
        # Generate test audio
        print("Generating test audio file...")
        audio_file = generate_test_audio()
        
        # Prepare request
        files = {'audio': ('test.wav', audio_file, 'audio/wav')}
        
        print("Sending POST request to /transcribe...")
        response = requests.post(url, files=files, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        print()
        
        if response.status_code == 200:
            data = response.json()
            print("✓ SUCCESS!")
            print()
            print("Response:")
            print(f"  Text: {data.get('text', '(empty)')}")
            print(f"  Word Count: {len(data.get('words', []))}")
            print()
            if data.get('words'):
                print("  First few words:")
                for word_data in data['words'][:5]:
                    print(f"    - {word_data.get('word')}: {word_data.get('confidence', 0):.2f}")
        else:
            print("✗ FAILED!")
            print(f"  Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("✗ CONNECTION ERROR!")
        print("  Backend server is not running on port 8000")
        print("  Please ensure the server is running:")
        print("    backend\\venv311\\Scripts\\python -m uvicorn backend.main:app --reload --port 8000")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    print("=" * 60)

if __name__ == "__main__":
    test_transcribe_endpoint()
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
