import math

def calculate_area(x1, y1, x2, y2, x3, y3):
    """Function to calculate area of a triangle given its three vertices."""
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return area

# Coordinates of vertices A, B, and C
Ax, Ay = 0, 0
Bx, By = 5, 0
Cx, Cy = 3, 3

# Call the function to calculate the area
area = calculate_area(Ax, Ay, Bx, By, Cx, Cy)

# Print the result
print("Area of triangle ABC is:", area)
