import numpy as np 
# Initial point P 
P = np.array([4, -2]) 
# (1) Reflection through Y-axis 
P_reflect_y = np.array([-P[0], P[1]]) 
# (11) Scaling in X-coordinate by factor 5 
P_scale_x = np.array([5* P[0], P[1]]) 
# (III) Rotation about origin through an angle pi/2 
angle = np.pi/2 
P_rotate = np.array([P[0]* np.cos(angle) - P[1]* np.sin(angle), P[0]* np.sin(angle) + P[1] * np.cos(angle)]) 
# (IV) Shearing in X-direction by 7/2 units 
shearing_factor = 7/2 
P_shear_x = np.array([P[0] + shearing_factor * P[1], P[1]]) 
#Print the transformed points 
print("Initial point P:", P) 
print("Reflection through Y-axis:", P_reflect_y) 
print("Scaling in X-coordinate by factor 5:", P_scale_x) 
print("Rotation about origin through an angle pi/2:", P_rotate) 
print("Shearing in X-direction by 7/2 units:", P_shear_x)

output:-
Initial point P: [ 4 -2]
Reflection through Y-axis: [-4 -2]
Scaling in X-coordinate by factor 5: [20 -2]
Rotation about origin through an angle pi/2: [2. 4.]
Shearing in X-direction by 7/2 units: [-3. -2.]
