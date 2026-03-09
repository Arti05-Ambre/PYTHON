import matplotlib.pyplot as plt  
import math  
pentagon = [(0,0), (2,0), (3,1),(1.5,3),(0,2)]  
theta = math.radians(60)  
dx, dy = 2,1 
transformed = [((x*math.cos(theta) - y*math.sin(theta)) + dx, 
               (x*math.sin(theta) +y*math.cos(theta)) + dy) for x,y in pentagon] 
def plot_poly(poly, color, label ):  
    xs= [p[0] for p in poly] + [poly[0][0]] 
    ys= [p[1] for p in poly] + [poly[0][1]] 
    plt.plot(xs, ys, '-o', color=color, label=label) 
plot_poly (pentagon, 'blue', 'Original')  
plot_poly(transformed, 'red' , 'Transformed')  
plt.title("Pentagon: Rotation + Translation") 
plt.legend()  
plt.axis('equal')  
plt.grid(True)  
plt.show() 
