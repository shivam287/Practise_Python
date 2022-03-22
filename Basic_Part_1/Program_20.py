# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to get a string which is n (non-negative integer) copies of a given string.


def Program_logic(user_string, no_of_copies):
    return user_string * no_of_copies


if __name__ == "__main__":
    user_str = input("Please enter your string: ")
    copies = int(input("Please enter the number of copies you want of your string: "))
    print(f"\nOutput:\n{Program_logic(user_str, copies)}")
