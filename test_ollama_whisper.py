"""
Test Ollama Whisper model for STT
"""

import requests
import base64
import wave
import struct


# Generate a simple test audio file
def generate_test_audio(filename="test_audio.wav"):
    sample_rate = 16000
    duration = 2
    frequency = 440

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)

        samples = []
        for i in range(int(sample_rate * duration)):
            sample = int(32767 * 0.3 * (i % 100 < 50))  # Square wave
            samples.append(sample)

        packed_data = struct.pack("<" + "h" * len(samples), *samples)
        wav_file.writeframes(packed_data)

    return filename


# Test Ollama Whisper
def test_ollama_whisper():
    print("Testing Ollama Whisper model...")

    # Generate test audio
    audio_file = generate_test_audio()
    print(f"Generated test audio: {audio_file}")

    # Read and encode audio
    with open(audio_file, "rb") as f:
        audio_data = f.read()

    audio_b64 = base64.b64encode(audio_data).decode("utf-8")

    # Try different API formats
    print("\n1. Testing with /api/generate endpoint...")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "dimavz/whisper-tiny:latest",
                "prompt": "Transcribe this audio:",
                "images": [audio_b64],
                "stream": False,
            },
            timeout=30,
        )
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {data}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n2. Testing with direct prompt...")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "dimavz/whisper-tiny:latest",
                "prompt": f"[AUDIO_DATA]{audio_b64}[/AUDIO_DATA]",
                "stream": False,
            },
            timeout=30,
        )
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {data}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_ollama_whisper()
