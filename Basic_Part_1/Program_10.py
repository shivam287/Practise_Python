# Date: 21-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

def n_number(n):
    return n + int(str(f"{n}{n}")) + int(str(f"{n}{n}{n}"))


if __name__ == "__main__":
    num = int(input("Please enter the desired number: "))
    print(f"Your computed value of n+nn+nnn: {n_number(num)}")
