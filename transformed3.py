import matplotlib.pyplot as plt  
import math  
triangle = [(1,1), (3,1), (2,3)]  
theta = math.radians(45)  
57 
 
transformed = [(- (x*math.cos(theta) - y*math.sin(theta)), 
               x*math.sin(theta) +y*math.cos(theta)) for x,y in triangle] 
def plot_tri(tri, color, label ):  
    xs= [p[0] for p in tri] + [tri[0][0]] 
    ys= [p[1] for p in tri] + [tri[0][1]] 
    plt.plot(xs, ys, '-o', color=color, label=label) 
plot_tri (triangle, 'blue', 'Original')  
plot_tri(transformed, 'red' , 'Transformed')  
plt.title("Triangle: Rotation + Reflection") 
plt.legend()  
plt.axis('equal')  
plt.grid(True)  
plt.show()
