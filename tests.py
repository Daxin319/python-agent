from functions.get_files_info import get_files_info


def test_get_files_info():
    # Test with current directory
    result1 = get_files_info("calculator", ".")
    print("Test 1 - Current directory:")
    print(result1)
    print("\n")

    # Test with pkg directory
    result2 = get_files_info("calculator", "pkg")
    print("Test 2 - pkg directory:")
    print(result2)
    print("\n")

    # Test with invalid directory outside working directory
    result3 = get_files_info("calculator", "/bin")
    print("Test 3 - Invalid directory (/bin):")
    print(result3)
    print("\n")

    # Test with parent directory
    result4 = get_files_info("calculator", "../")
    print("Test 4 - Parent directory:")
    print(result4)
    print("\n")

if __name__ == "__main__":
    test_get_files_info()
