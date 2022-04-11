# Date: 11-April-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import struct
import platform

if __name__ == "__main__":
    print("\nPlatform Type:")
    print(f"Platform 32 Bit or 64 Bit: {platform.architecture()[0]}")  # One Way
    print(f"Platform 32 Bit or 64 Bit: {struct.calcsize('P') * 8}")  # Another Way

    print("\nAdditional Information\n")

    print(f"OS Platform: {platform.machine()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Python Compiler: {platform.python_compiler()}")
