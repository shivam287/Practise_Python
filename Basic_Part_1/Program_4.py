# Date: 17-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi


def area(radius):
    """
    For calculating Area of a circle
    :param radius: radius of the circle.
    :return: area of circle
    """
    return pi * (radius ** 2)


if __name__ == "__main__":
    user_input = int(input("Please enter the radius of the circle: "))
    print(f"Area of the Circle: {format(area(user_input),'.4f')}")
