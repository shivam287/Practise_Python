# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while True:
        if (z % x == 0) and (z % y == 0):
            lcm_value = z
            break
        z += 1
    return lcm_value


if __name__ == "__main__":
    print("\nLeast Common Multiple Examples: \n")
    print(f"Least Common Multiple: {lcm(4, 6)}")
    print(f"Least Common Multiple: {lcm(15, 17)}")
