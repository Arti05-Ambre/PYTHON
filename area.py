import numpy as np

# Define the vertices of the triangle
A = np.array([0, 0])
B = np.array([5, 0])
C = np.array([3, 3])

# Calculate the side lengths of the triangle
AB = np.linalg.norm(B - A)
BC = np.linalg.norm(C - B)
CA = np.linalg.norm(A - C)

# Calculate the semiperimeter
s = (AB + BC + CA) / 2

# Calculate the area using Heron's formula
area = np.sqrt(s * (s - AB) * (s - BC) * (s - CA))

# Calculate the perimeter
perimeter = AB + BC + CA

# Print the results
print("Triangle ABC:")
print("Side AB:", AB)
print("Side BC:", BC)
print("Side CA:", CA)
print("Area:", area)
print("Perimeter:", perimeter)
