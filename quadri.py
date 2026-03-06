import matplotlib.pyplot as plt 
quadrilateral = [(1,1), (5,1), (6,4), (5,5)] 
quadri_closed = quadrilateral + [quadrilateral[0]]
x = [p[0] for p in quadri_closed]
y = [p[1] for p in quadri_closed]
plt.plot(x, y, marker='o')
plt.fill(x, y, color='skyblue', alpha=0.4)
plt.title("Quadrlateral Plot")
plt.grid(True)
plt.axis("equal")
plt.show()
