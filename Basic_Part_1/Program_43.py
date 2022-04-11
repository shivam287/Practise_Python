# Date: 11-April-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to get OS name, platform and release information.

from os import name
from sys import platform
from sysconfig import get_platform
from platform import system, release, machine, architecture

if __name__ == "__main__":
    print("\nPrinting the Required Output:")
    print(f"\nName of the operating system: {name}")
    print(f"Platform: {platform}")
    print(f"Name of the OS system: {system()}")
    print(f"Platform Version: {get_platform()}")
    print(f"Version of the operating system: {release()}")
    print(f"Platform Machine: {machine()}")
    print(f"Platform Architecture: {architecture()}")
