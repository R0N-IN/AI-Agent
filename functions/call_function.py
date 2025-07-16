from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
function_dictionary = {
        "get_file_content" : get_file_content,
        "get_files_info" : get_files_info,
        "run_python_file" : run_python_file,
        "write_file" : write_file
    }


def call_function(function_call_part, verbose=False):
    function_args = function_call_part.args 
    function_name = function_call_part.name 

    if verbose: 
        print(f"Calling function: {function_name}({function_args})")
    else: 
        print(f" - Calling function: {function_name}")

    function_result = function_dictionary[function_name]("./calculator",**function_args)

    try: 
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    except:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )