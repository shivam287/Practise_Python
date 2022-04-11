# Date: 11-April-2022
# Author: Shivam Mishra

# Problem Description:
# Write a python program to call an external command in Python.

from os import system

import psutil
from psutil import * # Using External Package. Use "pip install psutil" for installing the Package.

if __name__ == "__main__":
    print("\nCMD Line Command Output:\n")
    print(system('dir'))
    print(f"CPU Count: {psutil.cpu_count()}")  # Another way.
