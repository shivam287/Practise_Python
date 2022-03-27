# Date: 27-March-2022
# Author: Shivam Mishra

# Problem Description:
# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

def distance_bw_two_points(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


if __name__ == "__main__":
    points_1_coordinates = [int(val) for val in input("\nPlease enter x and y value of Point 1: ").split()]
    points_2_coordinates = [int(val) for val in input("Please enter x and y values of Point 2: ").split()]

    print(f"\nDistance bw two points is "
          f"{format(distance_bw_two_points(points_1_coordinates, points_2_coordinates), '.2f')} cm square")
