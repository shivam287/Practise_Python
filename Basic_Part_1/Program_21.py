# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

def odd_or_even(num):
    return f"Your Number {num} is Odd" if num % 2 != 0 else f"You number {num} is even"


if __name__ == "__main__":
    number = int(input("Please enter your number: "))
    print(f"Output: {odd_or_even(number)}")
