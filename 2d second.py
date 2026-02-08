import numpy as np 
# Define the point P 
P = np.array([4, -2]) 
# Define the transformation functions 
def rotate_about_origin(point, angle):
    # Rotation about origin through an angle
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle) 
    x = point[0] 
    y = point[1] 
    x_rotated = x * cos_theta - y * sin_theta 
    y_rotated = x * sin_theta + y * cos_theta 
    return np.array([x_rotated, y_rotated]) 
def scale_x(point, factor): 
    #Scaling in X-coordinate 
    x_scaled = point[0] * factor
    y_scaled = point[1]
    return np.array([x_scaled, y_scaled]) 

def uniform_scale(point, factor): 
    # Uniform scaling 
    x_scaled = point[0] * factor 
    y_scaled = point[1] * factor 
    return np.array([x_scaled, y_scaled]) 

def reflect_x_axis(point): 
    #Reflection through X-axis 
    x_reflected = point[0] 
    y_reflected = -point[1]
    return np.array([x_reflected, y_reflected])

#Apply the transformations to the point P 
angle = np.pi/3 
P_rotated = rotate_about_origin(P, angle) 
P_scaled_x = scale_x(P_rotated, 7) 
P_uniform_scaled = uniform_scale(P_scaled_x, -4) 
P_reflected_x_axis = reflect_x_axis(P_uniform_scaled)

# Print the transformed points 
print("Point P: ", P) 
print("After Rotation: ", P_rotated) 
print("After Scaling in X-Coordinate: ", P_scaled_x) 
print("After Uniform Scaling: ", P_uniform_scaled) 
print("After Reflection through X-axis: ", P_reflected_x_axis)

output:- 

Point P:  [ 4 -2]
After Rotation:  [3.73205081 2.46410162]
After Scaling in X-Coordinate:  [26.12435565  2.46410162]
After Uniform Scaling:  [-104.49742261   -9.85640646]
After Reflection through X-axis:  [-104.49742261    9.85640646]

