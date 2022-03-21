# Date: 21-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

if __name__ == "__main__":
    month = input("Please enter the Month: ")
    year = input("Please enter the Year: ")
    print(f"\nHere is your Calender:\n{calendar.month(int(year), int(month))}")
    