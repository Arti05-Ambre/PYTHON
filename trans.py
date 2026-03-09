import matplotlib.pyplot as plt 
import math  
triangle=[(0,0), (2,0), (1,1)]  
sx, sy =1.5,2 
dx, dy = 1, 2 
transformed= [(x*sx + dx, y*sy + dy) for x,y in triangle] 
def plot_triangle(tri, color, label ):  
    xs= [p[0] for p in tri] + [tri[0][0]] 
    ys= [p[1] for p in tri] + [tri[0][1]] 
    plt.plot(xs, ys, '-o', color=color, label=label) 
plot_triangle(triangle, 'blue', 'Original')  
plot_triangle(transformed, 'red' , 'Transformed')  
plt.title("Triangle: Scaling + Translation") 
plt.legend()  
plt.axis('equal')  
plt.grid(True)  
plt.show() 
