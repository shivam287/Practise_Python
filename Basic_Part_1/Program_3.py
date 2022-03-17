# Date: 17-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time

from datetime import datetime

if __name__ == "__main__":
    x = datetime.now()
    Today_Date_and_Time = x.strftime("%Y-%m-%d %H:%M:%S")
    print("Output:")
    print(f"Today's Date and Current Time is {Today_Date_and_Time}")
