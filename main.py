import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.schemas import *

from functions.call_function import call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#Read input to be used by the bot 
try: 
    prompt = sys.argv[1]
except IndexError:
    print("Usage: uv run main.py '<your prompt here>'")
    sys.exit(1)


#Functions declared as schemas 
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)
#Store conversation history
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]


#Define model and generate content    
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents = messages,
    config=types.GenerateContentConfig(tools=[available_functions],system_instruction=os.environ.get("system_prompt")))
#Filter non text parts 
text_parts = [
    part.text for part in response.candidates[0].content.parts
    if hasattr(part, "text") and part.text
    ]


#Check if the response contains function calls
try:
    function_call_part = response.function_calls[0]
    function_call_content = response.candidates[0].content
    for candidate in response.candidates: 
        messages.append(candidate.content)
except: 
    function_call_part = None
    function_call_content = None

#Optionally print verbose output
verbose = True if "--verbose" in sys.argv else False
if(function_call_part):
    function_call_result = call_function(function_call_part, verbose)
    messages.append(types.Content(role="user",parts=function_call_result.parts))

    try: 
        if verbose:
            print(f"User prompt: {prompt}")
            print("->", " ".join(text_parts))
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        else:
            print("->", " ".join(text_parts))
                
    except: 
        raise Exception("Fatal Exception: No content was found on the response ")
else:
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"-> {response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(f"Response: {response.text}")
