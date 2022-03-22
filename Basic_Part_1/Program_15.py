# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to get the volume of a sphere with radius 6.

from math import pi


def sphere_area(radius):
    return 4/3 * pi * radius ** 3


if __name__ == "__main__":
    rad = int(input("Please enter the Radius of the Sphere: "))
    print(f"\nRadius of Sphere: {rad}")
    print(f"Area of the Sphere: {format(sphere_area(rad), '.2f')} cm cube")
