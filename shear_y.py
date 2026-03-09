import matplotlib.pyplot as plt

triangle = [(0,0),(3,0),(1,2)]

def plot_poly(poly,color,label):
    xs=[p[0] for p in poly]+[poly[0][0]]
    ys=[p[1] for p in poly]+[poly[0][1]]
    plt.plot(xs,ys,'-o',color=color,label=label)
shear_y = [(x,y+0.5*x)for x,y in triangle]
plot_poly(triangle,'blue','Original')
plot_poly(shear_y,'red','Sheared Y-axis')

plt.legend()
plt.title("Shearing along Y-axis(k=0.5)")
plt.axis('equal')
plt.grid(True)
plt.show()
