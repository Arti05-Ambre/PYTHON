from sympy import*
    A=Point(2,5)
    B=Point(4,-13)
    A1=A.transform(Matrix([[2,4,0],[5,1,0],[0,0,1]]))
    B1=B.transform(Matrix([[2,4,0],[5,1,0],[0,0,1]]))
    L=Segment(A1,B1)
    L.midpoint
