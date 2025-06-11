import os

def get_files_info(working_directory, directory=None):
    if directory is None or directory == ".":
        target_dir_abs = os.path.abspath(working_directory)
    else:
        target_dir_abs = os.path.abspath(os.path.join(working_directory, directory))

    working_directory_abs = os.path.abspath(working_directory)

    if not target_dir_abs.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'

    if not os.path.isdir(target_dir_abs):
        return f'Error: The path "{directory}" is not a valid directory.'
    
    files_info = []
    for file_name in sorted(os.listdir(target_dir_abs)):
        file_path = os.path.join(target_dir_abs, file_name)
        is_dir = os.path.isdir(file_path)
        try:
            file_size = os.path.getsize(file_path) if not is_dir else 0
            files_info.append(f'- {file_name}: file_size: {file_size} bytes, is_dir={is_dir}')
        except OSError:
            files_info.append(f'- {file_name}: file_size: N/A, is_dir: {is_dir}')
                
    return "\n".join(files_info)