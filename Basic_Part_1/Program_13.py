# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# Global Comment, As if i define under main, extra tab was also getting printed.
statement = '''
a string that you "don't" have to escape
This
is a ....... multi-line
'''

if __name__ == "__main__":
    print(f"Printing Statement:\n{statement}")
