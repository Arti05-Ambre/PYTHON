import numpy as np 
# Define the initial points A and B 
A = np.array([3, 2]) 
B = np.array([2, -3]) 
#Transformation 1: Rotation about origin through an angle of pi/6 
angle_1 = np.pi/6 
rotation_matrix_1 = np.array([[np.cos(angle_1), -np.sin(angle_1)], [np.sin(angle_1), np.cos(angle_1)]]) 
A_rotated_1 = np.dot(rotation_matrix_1, A) 
B_rotated_1 = np.dot(rotation_matrix_1, B) 
#Transformation 2: Scaling in y-Coordinate by -4 units
scaling_matrix_2 = np.array([[1, 0], [0, -4]]) 
A_scaled_2 = np.dot(scaling_matrix_2, A_rotated_1) 
B_scaled_2 = np.dot(scaling_matrix_2, B_rotated_1)
#Transformation 3: Uniform scaling by -6.4 units
scaling_matrix_3 = np.array([[-6.4, 0], [0, -6.4]]) 
A_scaled_3 = np.dot(scaling_matrix_3, A_scaled_2) 
B_scaled_3 = np.dot(scaling_matrix_3, B_scaled_2)
#Transformation 4: Shearing in y-Direction by 5 units
shearing_matrix_4 = np.array([[1, 0], [0, 1]])
shearing_matrix_4[0, 1] = 5 
A_sheared_4 = np.dot(shearing_matrix_4, A_scaled_3) 
B_sheared_4 = np.dot(shearing_matrix_4, B_scaled_3) 
# Print the input and output points for each transformation
print("Input Point A:", A)
print("Input Point B:", B)
print("Transformation 1 - Rotation:")
print(" - Rotated Point A:", A_rotated_1)
print(" - Rotated Point B:", B_rotated_1)
print("Transformation 2 - Scaling in y-coordinate:")
print(" - Scaled Point A:", A_scaled_2)
print(" - Scaled Point B:", B_scaled_2)
print("Transformation 3 - Uniform Scaling:")
print(" - Scaled Point A:", A_scaled_3)
print(" - Scaled Point B:", B_scaled_3)
print("Transformation 4 - Shearing in y-Direction:")
print(" - Sheared Point A:", A_sheared_4)
print(" - Sheared Point B:", B_sheared_4)

Output:-
Input Point A: [3 2]
Input Point B: [ 2 -3]
Transformation 1 - Rotation:
 - Rotated Point A: [1.59807621 3.23205081]
 - Rotated Point B: [ 3.23205081 -1.59807621]
Transformation 2 - Scaling in y-coordinate:
 - Scaled Point A: [  1.59807621 -12.92820323]
 - Scaled Point B: [3.23205081 6.39230485]
Transformation 3 - Uniform Scaling:
 - Scaled Point A: [-10.22768775  82.74050067]
 - Scaled Point B: [-20.68512517 -40.91075101]
Transformation 4 - Shearing in y-Direction:
 - Sheared Point A: [403.47481562  82.74050067]
 - Sheared Point B: [-225.23888022  -40.91075101]

