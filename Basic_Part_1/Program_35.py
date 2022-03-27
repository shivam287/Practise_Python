# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program that will return true if the two given integer values are equal or
# their sum or difference is 5.

def Program_logic(num1, num2):
    return True if num1 == num2 or num1 + num2 == 5 or abs(num1 - num2) == 5 else False


if __name__ == "__main__":
    # number_1 = int(input("Please Enter Number 1: "))
    # number_2 = int(input("Please Enter Number 2: "))

    # Alternative way of taking multiple input in a Single Line.

    num_1, num_2 = [int(val) for val in input("Please Enter your 2 Numbers: ").split()]
    print(f"Here is your Output according to the Program Logic: {Program_logic(num_1, num_2)}")
