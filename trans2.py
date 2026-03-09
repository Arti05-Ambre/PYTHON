import matplotlib.pyplot as plt  
square = [(0,0), (2,0), (2,2), (0,2)]  
sx, sy = 2,1  
k = 0.5  
dx, dy = 1,1 
transformed = [(x*sx + k*y + dx, y*sy + dy) for x,y in square] 
def plot_poly(poly, color, label ):  
    xs= [p[0] for p in poly] + [poly[0][0]] 
    ys= [p[1] for p in poly] + [poly[0][1]] 
    plt.plot(xs, ys, '-o', color=color, label=label) 
plot_poly(square, 'blue', 'Original')  
plot_poly(transformed, 'red' , 'Transformed')  
plt.title("Square: Scaling + Shearing + Translation") 
plt.legend()  
plt.axis('equal')  
plt.grid(True)  
plt.show() 
