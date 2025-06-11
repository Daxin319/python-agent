# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python import run_python

def test_run_python():
    result1 = run_python("calculator", "main.py")
    print("Test 1 - Current directory:")
    print(result1)
    print("\n")

    result2 = run_python("calculator", "tests.py")
    print("Test 2 - tests.py:")
    print(result2)
    print("\n")
    
    result3 = run_python("calculator", "../main.py")
    print("Test 3 - ../main.py:")
    print(result3)
    print("\n")
    
    result4 = run_python("calculator", "nonexistent.py")
    print("Test 4 - nonexistent.py:")
    print(result4)
    print("\n")
    
if __name__ == "__main__":
    test_run_python()
    
# def test_write_file():
#     result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     print("Test 1 - Current directory:")
#     print(result1)
#     print("\n")
#     
#     result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print("Test 2 - pkg directory:")
#     print(result2)
#     print("\n")
#     
#     result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print("Test 3 - /tmp/temp.txt:")
#     print(result3)
#     print("\n")
#     
# if __name__ == "__main__":
#     test_write_file()
    
# def test_get_file_content():
#     result1 = get_file_content("calculator", "main.py")
#     print("Test 1 - Current directory:")
#     print(result1)
#     print("\n")
#     
#     result2 = get_file_content("calculator", "pkg/calculator.py")
#     print("Test 2 - pkg/calculator.py:")
#     print(result2)
#     print("\n")
#     
#     result3 = get_file_content("calculator", "/bin/cat")
#     print("Test 3 - /bin/cat:")
#     print(result3)
#     print("\n")
# 
# if __name__ == "__main__":
#     test_get_file_content()


# def test_get_files_info():
#     # Test with current directory
#     result1 = get_files_info("calculator", ".")
#     print("Test 1 - Current directory:")
#     print(result1)
#     print("\n")
# 
#     # Test with pkg directory
#     result2 = get_files_info("calculator", "pkg")
#     print("Test 2 - pkg directory:")
#     print(result2)
#     print("\n")
# 
#     # Test with invalid directory outside working directory
#     result3 = get_files_info("calculator", "/bin")
#     print("Test 3 - Invalid directory (/bin):")
#     print(result3)
#     print("\n")
# 
#     # Test with parent directory
#     result4 = get_files_info("calculator", "../")
#     print("Test 4 - Parent directory:")
#     print(result4)
#     print("\n")
# 
# if __name__ == "__main__":
#     test_get_files_info()
# 