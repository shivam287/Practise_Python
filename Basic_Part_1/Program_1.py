# Date: 17-March-2022
# Author: Shivam Mishra

# Problem Description:

# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high,
# Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
#       Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

twinkle_rhym = "Twinkle, twinkle, little star,\n\t" \
               "How I wonder what you are!\n\t\t" \
               "Up above the world so high,\n\t\t" \
               "Like a diamond in the sky.\n" \
               "Twinkle, twinkle, little star,\n\t" \
               "How I wonder what you are"

if __name__ == "__main__":
    print(f"Output: \n{twinkle_rhym}")
