<<<<<<< HEAD
import asyncio
import websockets
import os
import io
import wave
import math
import struct

async def test_stt_vad():
    uri = "ws://127.0.0.1:8000/ws/transcribe"
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            
            # Generate audio: 3 seconds of tone (speech proxy) + 2 seconds of silence
            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav_file:
                wav_file.setnchannels(1) # Mono
                wav_file.setsampwidth(2) # 16-bit
                wav_file.setframerate(16000) # 16kHz
                
                # Generate 3 seconds of 440Hz tone
                for i in range(16000 * 3):
                    value = int(32767.0 * 0.5 * math.sin(2.0 * math.pi * 440.0 * i / 16000.0))
                    wav_file.writeframes(struct.pack('<h', value))
                
                # Generate 2 seconds of silence
                wav_file.writeframes(b'\x00' * 16000 * 2)
            
            audio_data = buffer.getvalue()
            
            # Send in chunks to simulate real-time streaming
            chunk_size = 4096
            print(f"Sending {len(audio_data)} bytes of audio data in chunks...")
            
            for i in range(0, len(audio_data), chunk_size):
                chunk = audio_data[i:i+chunk_size]
                await websocket.send(chunk)
                await asyncio.sleep(0.01) # Simulate network delay
            
            print("Finished sending. Waiting for response...")
            try:
                # We might get multiple responses
                while True:
                    response = await asyncio.wait_for(websocket.recv(), timeout=10.0)
                    print(f"Received: '{response}'")
            except asyncio.TimeoutError:
                print("Timeout (expected if no more speech)")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(test_stt_vad())
=======
import asyncio
import websockets
import os
import io
import wave
import math
import struct

async def test_stt_vad():
    uri = "ws://127.0.0.1:8000/ws/transcribe"
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            
            # Generate audio: 3 seconds of tone (speech proxy) + 2 seconds of silence
            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav_file:
                wav_file.setnchannels(1) # Mono
                wav_file.setsampwidth(2) # 16-bit
                wav_file.setframerate(16000) # 16kHz
                
                # Generate 3 seconds of 440Hz tone
                for i in range(16000 * 3):
                    value = int(32767.0 * 0.5 * math.sin(2.0 * math.pi * 440.0 * i / 16000.0))
                    wav_file.writeframes(struct.pack('<h', value))
                
                # Generate 2 seconds of silence
                wav_file.writeframes(b'\x00' * 16000 * 2)
            
            audio_data = buffer.getvalue()
            
            # Send in chunks to simulate real-time streaming
            chunk_size = 4096
            print(f"Sending {len(audio_data)} bytes of audio data in chunks...")
            
            for i in range(0, len(audio_data), chunk_size):
                chunk = audio_data[i:i+chunk_size]
                await websocket.send(chunk)
                await asyncio.sleep(0.01) # Simulate network delay
            
            print("Finished sending. Waiting for response...")
            try:
                # We might get multiple responses
                while True:
                    response = await asyncio.wait_for(websocket.recv(), timeout=10.0)
                    print(f"Received: '{response}'")
            except asyncio.TimeoutError:
                print("Timeout (expected if no more speech)")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(test_stt_vad())
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
