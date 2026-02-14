import matplotlib.pyplot as plt
import numpy as np
vertices = np.array([[0,0],[1,0],[2,2],[1,4],[0,0]])
x = vertices[:, 0]
y = vertices[:, 1]
fig, ax=plt.subplots()
ax.plot(x, y, 'b',label='Polygon')
area = 0.5 * np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
perimeter = np.sum(np.sqrt(np.diff(x)**2+np.diff(y)**2))
print("Area of the polygon:",area)
print("perimeter of the polygon:",perimeter)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Polygon with Vertices(0,0),(1,0),(2,2),(1,4)')
ax.legend()
plt.grid(True)
plt.show()
