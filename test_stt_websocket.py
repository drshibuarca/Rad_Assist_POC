<<<<<<< HEAD
import asyncio
import websockets
import os
import io
import wave

async def test_stt():
    uri = "ws://127.0.0.1:8000/ws/transcribe"
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            
            # Generate a valid WAV file in memory
            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav_file:
                wav_file.setnchannels(1) # Mono
                wav_file.setsampwidth(2) # 16-bit
                wav_file.setframerate(16000) # 16kHz
                # 5 seconds of silence to trigger VAD and chunking
                wav_file.writeframes(b'\x00' * 32000 * 5)
            
            audio_data = buffer.getvalue()
            
            print(f"Sending {len(audio_data)} bytes of WAV data...")
            await websocket.send(audio_data)
            
            print("Waiting for response...")
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=10.0)
                print(f"Received: '{response}'")
            except asyncio.TimeoutError:
                print("Timeout waiting for response")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(test_stt())
=======
import asyncio
import websockets
import os
import io
import wave

async def test_stt():
    uri = "ws://127.0.0.1:8000/ws/transcribe"
    print(f"Connecting to {uri}...")
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            
            # Generate a valid WAV file in memory
            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav_file:
                wav_file.setnchannels(1) # Mono
                wav_file.setsampwidth(2) # 16-bit
                wav_file.setframerate(16000) # 16kHz
                # 5 seconds of silence to trigger VAD and chunking
                wav_file.writeframes(b'\x00' * 32000 * 5)
            
            audio_data = buffer.getvalue()
            
            print(f"Sending {len(audio_data)} bytes of WAV data...")
            await websocket.send(audio_data)
            
            print("Waiting for response...")
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=10.0)
                print(f"Received: '{response}'")
            except asyncio.TimeoutError:
                print("Timeout waiting for response")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(test_stt())
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
