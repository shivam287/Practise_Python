# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program that will accept the base and height of a triangle and compute the area.

def triangle_area(base, height):
    return 0.5 * base * height


if __name__ == "__main__":
    tri_base, tri_height = [int(val) for val in input("Please Enter the Base and Height of the Triangle: ").split()]
    print(f"Area of the triangle: {triangle_area(tri_base, tri_height)}")
