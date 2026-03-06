A=Point(1,1)
B=Point(-4,-1)
A1=A.transform(Matrix([[1,-2,0],[-2,1,0],[0,0,1]]))
B1=B.transform(Matrix([[1,-2,0],[-2,1,0],[0,0,1]]))
L=Segment(A1,B1)
L.points
print(f'the end  point is',L.points)
