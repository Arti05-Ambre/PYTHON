from sympy import*
x=Point(1,4)
y=Point(-4,3)
x.transform(Matrix([[1,0,0],[0,-1,0],[0,0,1]]))
