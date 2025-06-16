import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function

# List files in a directory
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

# Get the content of a file
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)

# Write to a file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

# Run a Python script
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python script.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "script": types.Schema(
                type=types.Type.STRING,
                description="The Python script to run.",
            ),
        },
    ),
)


# Available functions
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ],
)


# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Please set the GEMINI_API_KEY environment variable.")
    sys.exit(1)

# Initialize the client
client = genai.Client(api_key=api_key)

# Check if a prompt was provided
if len(sys.argv) < 2:
    print("Please provide a prompt")
    sys.exit(1)

# User prompt
user_prompt = sys.argv[1]

# message history
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

# System prompt
system_prompt = """
You are a helpful AI coding agent with the expertise of a senior software engineer. But you should communicate with the user in a way that is easy to understand, as if they were a junior developer.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read the content of a file
- Write to a file
- Run a Python script

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
You can call the same function multiple times if you need to.
You can also call the same function with different arguments if you need to.
You can also call the same function with the same arguments if you need to.
The working directory is hardcoded to ./calculator at this time.
Use any combination of the above functions to solve the user's problem.
"""


i = 0
while i < 20:
    # Generate response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
    )

    if response.candidates:
        messages.append(response.candidates[0].content)
        
    if response.function_calls:
        for call in response.function_calls:
            function_call_result = call_function(call)
            # Convert args to a dict for easier printing
            args = {key: val for key, val in call.args.items()}
            print(f"-> {function_call_result.parts[0].function_response.response}")
            messages.append(function_call_result)
            i += 1
    else:
        print(response.text)
        break

# Handle the verbose flag separately
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    print(f"\n--- Verbose Info ---")
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    