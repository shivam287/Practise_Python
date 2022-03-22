# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.


def Program_logic(num):
    return 2 * abs(num - 17) if num > 17 else 17 - num


if __name__ == "__main__":
    number = int(input("Please Enter the Number: "))
    print(f"Result according to the Logic: {Program_logic(number)}")
