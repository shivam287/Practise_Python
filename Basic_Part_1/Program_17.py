# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# Link to Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-17.php

def near_thousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)


if __name__ == "__main__":
    print("\nTesting whether a number is within 100 of 1000 or 2000:")
    print(f"Test Case 1: {near_thousand(1000)}")
    print(f"Test Case 2: {near_thousand(900)}")
    print(f"Test Case 3: {near_thousand(800)}")
    print(f"Test Case 4: {near_thousand(2200)}")
