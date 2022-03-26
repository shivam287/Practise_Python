# Date: 26-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to print out a set containing all the colors from color_list_1 which are
# not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

if __name__ == "__main__":
    color_list_1 = ["White", "Black", "Red"]
    color_list_2 = ["Red", "Green"]

    print(f"Colour List 1: {color_list_1}")
    print(f"Color List 2: {color_list_2}\n")

    print(f"Difference b/w Colour list 1: {set(color_list_1) - set(color_list_2)}")
    print(f"Difference b/w Colour list 2: {set(color_list_2) - set(color_list_1)}\n")

    # Another Solution (Good Use of inbuilt Method...)

    # print(f"Colour List 1: {color_list_1}")
    # print(f"Color List 2: {color_list_2}\n")
    #
    # print(f"Difference b/w Color List 1: {set(color_list_1).difference(color_list_2)}")
    # print(f"Difference b/w Color List 2: {set(color_list_2).difference(color_list_1)}")
