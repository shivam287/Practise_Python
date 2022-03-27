# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to sum of two given integers. However, if the sum is between 15 and 20 it will return 20.

def Program_logic(num1, num2):
    return 20 if 15 <= num1 + num2 <= 20 else num1 + num2


if __name__ == "__main__":
    # number_1 = int(input("Please Enter Number 1: "))
    # number_2 = int(input("Please Enter Number 2: "))

    # Alternative way of taking multiple input in a Single Line.

    num_1, num_2 = [int(val) for val in input("Please Enter your 2 Numbers: ").split()]
    print(f"Here is your Output according to the Program Logic: {Program_logic(num_1, num_2)}")
