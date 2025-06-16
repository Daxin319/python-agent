import os
import subprocess

def run_python(working_directory, script):
    if not os.path.exists(os.path.abspath(working_directory)):
        return f"Error: The directory {working_directory} does not exist"
    
    full_path = os.path.join(os.path.abspath(working_directory), script)

    if not os.path.exists(full_path):
        return f'Error: File "{script}" not found'
    if not os.path.commonpath([os.path.abspath(working_directory)]) in os.path.commonpath([os.path.abspath(working_directory), os.path.abspath(full_path)]):
        return f'Error: Cannot execute "{script}" as it is outside the permitted working directory'
        
    if not script.endswith('.py'): 
        return f'Error: File {script} is not a Python file'
        
    
    try:
        result = subprocess.run(['python', full_path], cwd=os.path.abspath(working_directory), timeout=30, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if len(output) == 0:
            return f'No output produced'
        if result.returncode != 0:
            return f'Error: Failed to execute {script}: Process exited with code {result.returncode}\nOutput:\n{output}'
        
        return f'Output:\n{output}\nRan {script} successfully\n'
    except subprocess.CalledProcessError as e:
        return f'Error: Error processing python file {script}: {e}'
    
    
    