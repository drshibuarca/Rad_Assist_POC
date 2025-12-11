<<<<<<< HEAD
import requests

# Test the REST API endpoint
url = "http://localhost:8000/transcribe"

# Read a sample WebM file (you can record one using the browser test page and save it)
# For now, create a simple test that shows how to use the API

print("Testing /transcribe endpoint...")
print(f"URL: {url}")
print()
print("To test manually:")
print("1. Record audio in browser and save as test.webm")
print("2. Run: python test_transcribe_endpoint.py")
print()
print("Or use cURL:")
print(f"curl -X POST {url} -F 'audio=@test.webm'")
=======
import requests

# Test the REST API endpoint
url = "http://localhost:8000/transcribe"

# Read a sample WebM file (you can record one using the browser test page and save it)
# For now, create a simple test that shows how to use the API

print("Testing /transcribe endpoint...")
print(f"URL: {url}")
print()
print("To test manually:")
print("1. Record audio in browser and save as test.webm")
print("2. Run: python test_transcribe_endpoint.py")
print()
print("Or use cURL:")
print(f"curl -X POST {url} -F 'audio=@test.webm'")
>>>>>>> 533fb4b11c272a6a418375a1b2219f1c766b90bb
