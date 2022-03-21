# Date: 21-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

if __name__ == "__main__":
    exam_st_date = (11, 12, 2014)
    exam_format_date = ' / '.join([str(val) for val in list(exam_st_date)])
    print(f"The Examination will start from : {exam_format_date}")

    # Solution 2
    # exam_st_date = (11, 12, 2014)
    # print("The examination will start from : %i / %i / %i" % exam_st_date)
