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
