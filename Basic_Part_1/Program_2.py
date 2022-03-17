# Date: 17-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to get the Python version you are using.

import sys  # Solution 1
import platform  # Solution 2

if __name__ == "__main__":
    print("Solution 1:")
    print(f"The Current Version you are using - {sys.version}\n")
    print("Solution 2:")
    print(f"The Current Version you are using - {platform.python_version()}")
    print("This only gives the Version that we are using but not the Extra Information.")
