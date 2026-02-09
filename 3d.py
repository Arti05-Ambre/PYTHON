import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def rotate_yz_plane(point):
    x,y,z = point
    new_y = y*math.cos(math.radians(90))-z*math.sin(math.radians(90))
    new_z = y*math.sin(math.radians(90))+z*math.cos(math.radians(90))
    return[x,new_y,new_z]
point = [1,2,3]
rotated_point=rotate_yz_plane(point)
x_original,y_original,z_original = point
x_rotated,y_rotated,z_rotated = rotated_point
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_original,y_original,z_original, color='red',label='Original Point')
ax.scatter(x_rotated,y_rotated,z_rotated, color='blue', label='Rotated Point')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rotation through YZ-plane(Y-axis) by 90')
ax.legend()
plt.show()             
