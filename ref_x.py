import matplotlib.pyplot as plt

triangle = [(0,0),(3,0),(1,2)]

def plot_poly(poly,color,label):
    xs=[p[0] for p in poly]+[poly[0][0]]
    ys=[p[1] for p in poly]+[poly[0][1]]
    plt.plot(xs,ys,'-o',color=color,label=label)
ref_x= [(x,-y)for x,y in triangle]
plot_poly(triangle,'blue','Original')
plot_poly(ref_x,'red','Reflection X-axis')

plt.legend()
plt.title("Reflection over X-axis")
plt.axis('equal')
plt.grid(True)
plt.show()
