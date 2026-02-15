import numpy as np 
# Define the original point P 
P = np.array([-2, 4]) 
#Transformation 1: Shearing in Y direction by 7 units 
shearing_Y = np.array([[1, 0], [7, 1]]) 
P_transformed1 = np.dot(shearing_Y, P) 
#Transformation 2: Scaling in X and Y direction by 7/2 and 7 units respectively 
scaling_XY = np.array([[7/2, 0], [0, 7]]) 
P_transformed2 = np.dot(scaling_XY, P) 
#Transformation 3: Shearing in X and Y direction by 4 and 7 units respectively 
shearing_XY = np.array([[1, 4], [7, 1]]) 
P_transformed3 = np.dot(shearing_XY, P) 
#Transformation 4: Rotation about origin by an angle of 60 degrees 
angle = np.radians(60) 
rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) 
P_transformed4 = np.dot(rotation, P) 
# Print the transformed points 
print("Original Point P: {}".format(P)) 
print("Transformation 1: Shearing in Y direction by 7 units: {}".format(P_transformed1)) 
print("Transformation 2: Scaling in X and Y direction by 7/2 and 7 units respectively: {}".format(P_transformed2)) 
print("Transformation 3: Shearing in X and Y direction by 4 and 7 units respectively: {}".format(P_transformed3)) 
print("Transformation 4: Rotation about origin by an angle of 60 degrees: {}".format(P_transformed4)) 
