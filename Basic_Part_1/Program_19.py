# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to get a new string from
# a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.


def program_logic(user_string):
    return user_string if user_string.casefold().startswith('is') else 'Is' + user_string


if __name__ == "__main__":
    user_str = input("Please enter your string: ")
    print(f"Result according to the Program Logic: {program_logic(user_str)}")
