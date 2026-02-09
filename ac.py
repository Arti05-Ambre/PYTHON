import math
X = [1,2]
Y = [2,-2]
Z = [-1,2]
def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
XY = distance(X,Y)
YZ = distance(Y,Z)
XZ = distance(X,Z)
perimeter = XY + YZ + XZ
s= perimeter/2
area = math.sqrt(s*(s-XY)*(s-YZ)*(s-XZ))
print("Length of XY:",XY)
print("Length of YZ:",YZ)
print("Length of XZ:",XZ)
print("Perimeter:",perimeter)
print("Area:",area)                     
                     
