# Date: 17-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program which accepts the user's first and
# last name and print them in reverse order letter by letter
# with a space between them.


def word_reverser(value):
    values = list(value)
    return values[::-1]


if __name__ == "__main__":
    first_name = input("Please Enter First Name: ")
    last_name = input("Please Enter Last Name: ")
    print(f"Your name in Reverse Oder with Space:\n "
          f"{' '.join([val for val in word_reverser(last_name)])} - "
          f"{' '.join([val for val in word_reverser(first_name)])}")
