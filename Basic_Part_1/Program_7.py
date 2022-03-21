# Date: 21-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

from os import path, listdir

if __name__ == "__main__":
    i = 1
    script_path = input("Please Enter Path of the Folder where Files is Present: ")
    # Work for a List of Files
    for files in listdir(script_path):
        print(f"{i}. File Name: {files}")
        print(f">> File Extension: {path.splitext(files)[1][1:].strip().lower()}")
        # print(f">> File Extension: {files.split('.')[-1]}")  # Using Solution 2 in the scenario where
        # there is multiples files
        i += 1

    # Solution 2

    # filename = input("Input the Filename: ")
    # f_extns = filename.split(".")  # Returns a List with two elements, The whole path of the files with file name and
    # # Extension as second element.
    # print("The extension of the file is : " + repr(f_extns[-1]))  # Printing the Second Element.
