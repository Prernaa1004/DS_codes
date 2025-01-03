import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([3,4,5,2,1,2])
d=np.ones((2,3))
c=np.full((3,2),2)
print(d)

print(c)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)
print(a+b)
print(a*b)

print(np.sin(a))

#matrix multiplication
mat=np.matmul(c,d)
print(mat)

#determinant
det=np.linalg.det(mat)
print(det)
