import numpy as np
A = np.array([0,0])
B = np.array([6,0])
C = np.array([4,4])
AB = np.linalg.norm(B-A)
BC = np.linalg.norm(C-B)
CA = np.linalg.norm(A-C)
s = (AB+BC+CA)/2
area = np.sqrt(s*(s-AB)*(s-BC)*(s-CA))
perimeter=AB+BC+CA
print("Triangle ABC:")
print("Side AB:",AB)
print("Side BC:",BC)
print("Side CA:",CA)
print("Area:", area)
print("Perimeter:",perimeter)
