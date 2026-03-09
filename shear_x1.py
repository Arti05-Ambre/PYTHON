import matplotlib.pyplot as plt 
import math  
triangle=[(0,0), (3,0), (1,2)]  
scaled = [(x*2, y*1.5) for x,y in triangle] 
theta = math.pi/2 
rotated = [(x*math.cos(theta)-y*math.sin(theta), 
            x*math.sin(theta)+y*math.cos(theta)) for x,y in scaled] 
transformed=[(x+2, y+1) for x, y in rotated] 
def plot_poly(poly, color, label ):  
    xs= [p[0] for p in poly] + [poly[0][0]] 
    ys= [p[1] for p in poly] + [poly[0][1]] 
    plt.plot(xs, ys, '-o', color=color, label=label) 
shear_x = [(x + 1*y, y) for x,y in triangle]
plot_poly(triangle, 'blue', 'Original')  
plot_poly(transformed, 'red' , 'Transformed')  
plt.title("Combined Transformation on Triangle") 
plt.legend()  
plt.axis('equal')  
plt.grid(True)  
plt.show() 
