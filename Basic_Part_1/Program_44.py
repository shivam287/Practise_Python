# Date: 11-April-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to locate Python site-packages.

from site import getsitepackages

if __name__ == "__main__":
    print(f"\nYour Python Site Package Location: {getsitepackages()}")
