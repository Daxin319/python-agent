import os
import subprocess

def run_python(working_directory, file_path):
    if not os.path.exists(os.path.abspath(working_directory)):
        return f"Error: The directory {working_directory} does not exist"
    
    full_path = os.path.join(os.path.abspath(working_directory), file_path)

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found'
    if not os.path.commonpath([os.path.abspath(working_directory)]) in os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(full_path)]):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
    if not file_path.endswith('.py'): 
        return f'Error: File {file_path} is not a Python file'
        
    
    try:
        result = subprocess.run(['python', full_path], cwd=os.path.abspath(working_directory), timeout=30, capture_output=True, text=True)
        if len(result.stdout) == 0:
            return f'No output produced'
        if result.returncode != 0:
            return f'Error: Failed to execute {file_path}: Process exited with code {result.returncode}'
        
        return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nRan {file_path} successfully\n'
    except subprocess.CalledProcessError as e:
        return f'Error: Error processing python file {file_path}: {e}'
    
    
    