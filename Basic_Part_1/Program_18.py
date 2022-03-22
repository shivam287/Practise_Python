# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.


def program_logic(n1, n2, n3):
    return 3 * (n1 + n2 + n3) if n1 == n2 == n3 else n1 + n2 + n3


if __name__ == "__main__":
    num1 = int(input("PLease enter number 1: "))
    num2 = int(input("PLease enter number 2: "))
    num3 = int(input("Please enter number 3: "))
    print(f"Result according to the Program Logic: {program_logic(num1, num2, num3)}")
