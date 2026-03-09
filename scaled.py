import matplotlib.pyplot as plt

triangle = [(0,0),(3,0),(1,2)]


def plot_poly(poly,color,label):
    xs=[p[0] for p in poly]+[poly[0][0]]
    ys=[p[1] for p in poly]+[poly[0][1]]
    plt.plot(xs,ys,'-o',color=color,label=label)
scaled = [(x*2,y*1.5)for x,y in triangle]

plot_poly(triangle,'blue','Original')
plot_poly(scaled,'red','scaled')

plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
