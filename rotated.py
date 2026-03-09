import matplotlib.pyplot as plt
import math
triangle = [(0,0),(3,0),(1,2)]


theta = math.pi/2
rotated = [(x*math.cos(theta)-y*math.sin(theta),x*math.sin(theta)+y*math.cos(theta))for x,y in triangle]

def plot_poly(poly,color,label):
    xs=[p[0] for p in poly]+[poly[0][0]]
    ys=[p[1] for p in poly]+[poly[0][1]]
    plt.plot(xs,ys,'-o',color=color,label=label)

plot_poly(triangle,'blue','Original')
plot_poly(rotated,'red','Rotated')

plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
