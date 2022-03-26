# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to concatenate all elements in a list into a string and return it.

def Program_logic(user_list):
    return ", ".join(str(value) for value in user_list)


if __name__ == "__main__":
    user_input = [int(val) for val in input("Please Enter your Number with a Space: ").split()]
    print(f"Here is your List Value String: {Program_logic(user_input)}")
