import numpy as np
import matplotlib.pyplot as plt
vertices = np.array([[0,0],[1 ,0],[2,2],[1,4]])
x = vertices[:, 0]
y = vertices[:, 1]
plt.plot(x,y,'b-',label='Polygon')
plt.plot(x,y,'bo')
plt.xlabel('X')
plt.xlabel('Y')
plt.title('Polygon with Vertices')
plt.legend()
def calculate_area(vertices):
    x = vertices[:, 0]
    y = vertices[:, 1]
    return 0.5* np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
area=calculate_area(vertices)
perimeter = np.sum(np.sum(np.sqrt(np.sum(np.diff(vertices,axis=0)**2,axis=1))))
print("Area of the polygon:", area)
print("Perimeter of the polygon:",perimeter)
plt.show()
        
