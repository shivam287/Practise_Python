# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
    return "Inputs must be integers!" if not (isinstance(a, int) and isinstance(b, int)) else a + b


if __name__ == "__main__":
    print("\nSome Examples: \n")
    print(f"Example 1: {add_numbers(10, 20)}")
    print(f"Example 2: {add_numbers(10, 20.23)}")
    print(f"Example 3: {add_numbers('5', 6)}")
    print(f"Example 4: {add_numbers('5', '6')}")
