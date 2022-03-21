# Date: 21-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

if __name__ == "__main__":
    print(f"1. abs aka Absolute Function description: {abs.__doc__}")
    print(f">> Example: '-1' in abs(-1) gives {abs(-1)}, \n   which is the value for that Number")

    print("\nAnother Example ...\n")
    print(f"2. len aka Length Function Description: {len.__doc__}")
