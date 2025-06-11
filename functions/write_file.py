import os

def write_file(working_directory, file_path, content):
    if not os.path.exists(os.path.abspath(working_directory)):
        return f"Error: The directory {working_directory} does not exist"
    
    if os.path.isabs(file_path):
        if not os.path.commonpath([os.path.abspath(working_directory)]) in os.path.commonpath([os.path.abspath(working_directory), file_path]):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
    full_path = os.path.join(os.path.abspath(working_directory), file_path)
    
    directory = os.path.dirname(full_path)
    os.makedirs(directory, exist_ok=True)
    
    with open(full_path, 'w') as file:
        file.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'   