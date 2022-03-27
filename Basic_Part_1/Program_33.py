# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def Program_logic(num1, num2, num3):
    return 0 if num1 == num2 or num2 == num3 or num1 == num3 else num1 + num2 + num3


if __name__ == "__main__":
    # number_1 = int(input("Please Enter Number 1: "))
    # number_2 = int(input("Please Enter Number 2: "))
    # number_3 = int(input("Please Enter Number 3: "))

    # Alternative way of taking multiple input in a Single Line.

    num_1, num_2, num_3 = [int(val) for val in input("Please Enter your 3 Numbers: ").split()]
    print(f"Here is your Output according to the Program Logic: {Program_logic(num_1, num_2, num_3)}")
