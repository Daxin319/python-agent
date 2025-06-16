from google.genai import types
from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    # Convert function call args to a Python dict
    args = {key: val for key, val in function_call_part.args.items()}

    if verbose:
        print(f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}")

    # Add working directory to args, which all functions expect
    args["working_directory"] = "./calculator"

    # Route to the appropriate function
    if function_name == "get_files_info":
        result = get_files_info(**args)
    elif function_name == "get_file_content":
        result = get_file_content(**args)
    elif function_name == "write_file":
        result = write_file(**args)
    elif function_name == "run_python_file":
        result = run_python(**args)
    else:
        result = f"Error: Unknown function: {function_name}"

    # Return the result in the format the model expects
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )