# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(x, y):
    gcd_default = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):  # Running the loop in Backward
        if x % k == 0 and y % k == 0:
            gcd_default = k
            break
    return gcd_default


if __name__ == "__main__":
    print("\nGreatest Common Divisor Examples: \n")
    print(f"GCD of 12 & 17: {gcd(17, 12)}")
    print(f"GCD of 4 & 6: {gcd(6, 4)}")
    print(f"GCD of 336 & 360: {gcd(336, 360)}")
