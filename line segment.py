import math

# Define the coordinates of points A and B
xA, yA = 0, 7
xB, yB = 5, 2

# Calculate the length of the line segment using the distance formula
length = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Calculate the midpoint of the line segment
midpoint_x = (xA + xB) / 2
midpoint_y = (yA + yB) / 2

# Print the equation of the line passing through A and B
print("The equation of the line passing through A and B is:")
print(f"y - {yA} = {(yB - yA) / (xB - xA)}(x - {xA})")

# Print the length and midpoint of the line segment
print(f"Length of the line segment: {length}")
print(f"Midpoint of the line segment: ({midpoint_x}, {midpoint_y})")
