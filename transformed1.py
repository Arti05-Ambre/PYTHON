import matplotlib.pyplot as plt

triangle = [(0,0),(3,0),(1,2)]
dx,dy = 2,3

transformed = [(x+dx, y+dy) for x,y in triangle]

def plot_poly(poly,color,label):
    xs=[p[0] for p in poly]+[poly[0][0]]
    ys=[p[1] for p in poly]+[poly[0][1]]
    plt.plot(xs,ys,'-o',color=color,label=label)

plot_poly(triangle,'blue','Original')
plot_poly(transformed,'red','Translated')

plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
