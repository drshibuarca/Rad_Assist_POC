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
    with wave.open(wav_buffer, "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)

        # Pack samples as 16-bit integers
        packed_data = struct.pack("<" + "h" * len(audio_data), *audio_data)
        wav_file.writeframes(packed_data)

    wav_buffer.seek(0)
    return wav_buffer


url = "http://localhost:8000/transcribe"
print(f"Testing STT at {url}")
print("-" * 50)

audio_file = generate_test_audio()
files = {"audio": ("test.wav", audio_file, "audio/wav")}

try:
    response = requests.post(url, files=files, timeout=30)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
