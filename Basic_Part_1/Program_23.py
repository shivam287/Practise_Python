# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

def Program_Logic(user_string, n):
    return user_string[0:2] * n if len(user_string) > 2 else user_string * 2


if __name__ == "__main__":
    user_str = input("Please Enter your String: ")
    number = int(input("Please enter the Number, the times you want to print the String: "))
    print(f"Here is your Output according to the Program_logic: \n{Program_Logic(user_str, number)}")
