# Date: 11-April-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to check whether a file exists.

from os import path, listdir

if __name__ == "__main__":
    print(f"Does Program_1 exists or not: {path.exists('Program_1.py')}")
    print(f"Does Main.py exists or not: {path.exists('main.py')}")
