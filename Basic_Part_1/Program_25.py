# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def Program_Logic(user_value):
    return True if user_value in [1, 5, 8, 3] else False


if __name__ == "__main__":
    user_input = int(input("Please Enter your Number: "))
    print(f"The Enter Number is present in the List: {Program_Logic(user_input)}")
