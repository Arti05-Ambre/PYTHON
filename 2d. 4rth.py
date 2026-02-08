import numpy as np
# Define the original points A and B 
A = np.array([5, 3])
B = np.array([1, 4])
# Transformation 1: Rotate about origin through an angle of pi/3 
angle = np.pi/3 
rotation = np.array([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]]) 
A_transformed1 = np.dot(rotation, A) 
B_transformed1 = np.dot(rotation, B)
# Transformation 2: Uniform scaling by -0.5 units 
scaling_uniform = np.array([[-0.5, 0], [0, -0.5]]) 
A_transformed2 = np.dot(scaling_uniform, A_transformed1) 
B_transformed2 = np.dot(scaling_uniform, B_transformed1) 
# Transformation 3: Scaling in Y-axis by 5 units 
scaling_Y = np.array([[1, 0], [0, 5]]) 
A_transformed3 = np.dot(scaling_Y, A_transformed2) 
B_transformed3 = np.dot(scaling_Y, B_transformed2) 
# Transformation 4: Shearing in X and Y direction by 3 and 4 units respectively 
shearing_XY = np.array([[1, 3], [4, 1]]) 
A_transformed4 = np.dot(shearing_XY, A_transformed3) 
B_transformed4 = np.dot(shearing_XY, B_transformed3) 
# Print the transformed points 
print("Original Point A: {}".format(A))
print("Original Point B: {}".format(B)) 
print("Transformation 1: Rotate about origin through an angle of pi/3")
print("A transformed1: {}".format(A_transformed1))
print("B transformed1: {}".format(B_transformed1))
print("Transformation 2: Uniform scaling by 0.5 units")
print("A transformed2: {}".format(A_transformed2))
print("B transformed2: {}".format(B_transformed2))
print("Transformation 3: Scaling in Y-axis by 5 units")
print("A transformed3: {}".format(A_transformed3))
print("B transformed3: {}".format(B_transformed3))
print("Transformation 4: Shearing in X and Y direction by 3 and 4 units respectively")
print("A transformed4: {}".format(A_transformed4))
print("B transformed4: {}".format(B_transformed4))

Output:-
Original Point A: [5 3]
Original Point B: [1 4]
Transformation 1: Rotate about origin through an angle of pi/3
A transformed1: [-0.09807621  5.83012702]
B transformed1: [-2.96410162  2.8660254 ]
Transformation 2: Uniform scaling by 0.5 units
A transformed2: [ 0.04903811 -2.91506351]
B transformed2: [ 1.48205081 -1.4330127 ]
Transformation 3: Scaling in Y-axis by 5 units
A transformed3: [  0.04903811 -14.57531755]
B transformed3: [ 1.48205081 -7.16506351]
