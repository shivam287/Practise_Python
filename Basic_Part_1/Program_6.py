# Date: 21-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program which accepts a sequence of comma-separated
# numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

if __name__ == "__main__":
    value = 'run'
    list_value = []
    while value == 'run':
        print("Type exit for exit and seeing your entered values ...")
        value = input("Please enter the Value, You want in the List: ")
        if value == 'exit':
            break
        else:
            list_value.append(int(value))
            value = 'run'

    print(f"\nUser Entered List: {list_value}")
    print(f"List to Tuple: {tuple(list_value)}")

    # Solution 2...

    # values = input("Input some comma separated numbers : ")
    # list_values = values.split(",")
    # print(list_values)
    # tuple_values = tuple(list_values)
    # print('List : ', list_values)
    # print('Tuple : ', tuple_values)
