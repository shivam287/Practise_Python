# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def solution(x, y):
    return (x + y) ** 2


if __name__ == "__main__":
    print("\nFor the Formula a + b whole square, Please Enter a and b,")
    a, b = [int(val) for val in input("Please enter a and b here: ").split()]
    print(f"\nHere is Your output: {solution(a, b)}")
