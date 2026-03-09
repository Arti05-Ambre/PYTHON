import matplotlib.pyplot as plt

triangle = [(0,0),(3,0),(1,2)]

def plot_poly(poly,color,label):
    xs=[p[0] for p in poly]+[poly[0][0]]
    ys=[p[1] for p in poly]+[poly[0][1]]
    plt.plot(xs,ys,'-o',color=color,label=label)
shear_x = [(x+1*y,y)for x,y in triangle]
plot_poly(triangle,'blue','Original')
plot_poly(shear_x,'red','Sheared X-axis')

plt.legend()
plt.title("Shearing along X-axis(k=1)")
plt.axis('equal')
plt.grid(True)
plt.show()
