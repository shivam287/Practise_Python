# Date: 22-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to count the number 4 in a given list.

# # Part of Solution 2
# def list_count_4(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count = count + 1
#
#     return count


if __name__ == "__main__":
    sample_list = ['4', '4', '5', '6', '7', '2', '4', '10']
    print(f"\nSample List: {sample_list}\nCount of '4' in the list: {sample_list.count('4')}")

    # # Solution 2
    # print(list_count_4([1, 4, 6, 7, 4]))
    # print(list_count_4([1, 4, 6, 4, 7, 4]))
