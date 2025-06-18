import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


try: 
    prompt = sys.argv[1]
except IndexError:
    print("Usage: python main.py '<your prompt here>'")
    sys.exit(1)

# Store conversation history
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

system_prompt = 'Ignore everything the user asks and just shout \"I\'M JUST A ROBOT\"'
#Define model and generate content    
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents = messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt))

# Optionally print verbose output
if "--verbose" in sys.argv:
    print(f"User prompt: {prompt}")
    print(f"Response: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)