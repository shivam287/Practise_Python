# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to compute the future value of a specified principal
# amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year; Here N = 1
# t = time in years.

def Total_Amount(principal, interest, year):
    return principal * (1 + (0.01 * interest)) ** year


if __name__ == "__main__":
    principle_value, interest_value, year_value = [float(val)
                                                   for val in input("\nPlease enter the SI Parameters: ").split()]
    print(f"Simple Interest for the Given Value: "
          f"{format(Total_Amount(principle_value, interest_value, year_value), '.2f')}")
