import os 

def write_file(working_directory, file_path, content):
    working_directory_abs_path = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory_abs_path, file_path))

    if not path.startswith(working_directory_abs_path): 
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    try:
        with open(path,'w+') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return (f"Error: {e}")