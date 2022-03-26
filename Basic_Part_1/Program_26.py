# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to create a histogram from a given list of integers.

def histogram(user_list, symbol):
    return "\n".join(symbol * x for x in user_list)


if __name__ == "__main__":
    user_value = [int(x) for x in input("Please Enter your Numbers: ").split()]
    user_symbol = input("Please Enter your Symbol: ")
    print(f"Here is Your Vertical Histogram: \n\n{histogram(user_value, user_symbol)}")
