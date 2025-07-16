import os

#note: returning strings for the LLM to use them 
def get_files_info(working_directory, directory=None):
    dir_name = (directory or '').strip('/') or './'
    working_directory_abs_path = os.path.abspath(working_directory)
    
    full_path = os.path.abspath(os.path.join(working_directory_abs_path, dir_name))

    if not full_path.startswith(working_directory_abs_path): 
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(full_path): 
        return f'Error: "{directory}" is not a directory'
    dir_content = os.listdir(full_path)
    metadata_str = ""
    
    for item_name in dir_content: 
        item_path = os.path.join(full_path,item_name)
        try: 
            item_metadata = os.stat(item_path)
            metadata_str += f"- {item_name} file_size={item_metadata.st_size} bytes, is_dir={os.path.isdir(item_path)}\n" 
        except Exception as e: 
            return (f"Error: {e}")
    return metadata_str
