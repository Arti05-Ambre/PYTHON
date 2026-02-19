from sympy import*
    A=Point(2,4)
    B=Point(3,2)
    A1=A.transform(Matrix([[3,-6,0],[2,1,0],[0,0,1]]))
    B1=B.transform(Matrix([[3,-6,0],[2,1,0],[0,0,1]]))
    L=Segment(A1,B1)
    L.slope
    print(f'line segment slope is',L.slope)
