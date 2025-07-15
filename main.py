import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.schemas import *


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


try: 
    prompt = sys.argv[1]
except IndexError:
    print("Usage: python main.py '<your prompt here>'")
    sys.exit(1)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
# Store conversation history
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]


#Define model and generate content    
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents = messages,
    config=types.GenerateContentConfig(tools=[available_functions],system_instruction=os.environ.get("system_prompt")))

# Check if the response contains function calls
function_call_part = response.function_calls[0]
function_call_content = response.candidates[0].content

# Optionally print verbose output
if "--verbose" in sys.argv:
    print(f"User prompt: {prompt}")
    if(function_call_part):
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        print(f"Response: {response.text}")
    else:
        print(f"Response: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)