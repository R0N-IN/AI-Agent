from google.genai import types
# Define schemas for the functions(python files) that can be used by the LLM

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="List the full content of the specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content from, relative to the working directory. If not provided just return the result",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the specified python file if you don't get the path, just try to run it on the current working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be run, relative to the working directory. If not provided just return the result",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Run the specified python file using python3 'name of the file' syntax",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content from, relative to the working directory. If not provided just return the result",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written on the file",
            ),
        },
    ),
)
# schema_get_files_info = types.FunctionDeclaration(
#     name="get_file_content",
#     description="Store the file content in a string, if the number of characters exceeds 10000 it truncates the file.",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "file": types.Schema(
#                 type=types.Type.STRING,
#                 description="The file to get the content from, relative to the working directory. If not provided, lists files in the working directory itself.",
#             ),
#         },
#     ),
# )
