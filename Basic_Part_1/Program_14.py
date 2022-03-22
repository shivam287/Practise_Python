# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

if __name__ == "__main__":
    d0 = date(2014, 7, 2)
    d1 = date(2014, 7, 11)
    delta = d1 - d0
    print(f"Date Difference: {delta.days} Days")
    print(f"Difference in hrs: {delta.days * 24} hours")
