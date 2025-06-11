import os

def get_file_content(working_directory, file_path):
    if not os.path.exists(os.path.abspath(working_directory)):
        return f"Error: The directory {working_directory} does not exist"
    
    if os.path.isabs(file_path):
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if not os.path.commonpath([os.path.abspath(working_directory)]) in os.path.commonpath([os.path.abspath(working_directory), file_path]):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else:
        full_path = os.path.join(os.path.abspath(working_directory), file_path)
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(os.path.join(working_directory, file_path), 'r') as file:
        file_string = file.read(10000)
        if len(file_string) >= 10000:
            file_string += f'\n[File "{file_path}" truncated to 10000 characters]'
        return file_string