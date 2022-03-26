# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to test whether a passed letter is a vowel or not.

def vowel_checker(user_value):
    return True if user_value in ['a', 'e', 'i', 'o', 'u'] else False


if __name__ == "__main__":
    user_input = input("Please Enter Your Letter: ")
    print(f"Entered Letter is a Vowel: {vowel_checker(user_input)}")
