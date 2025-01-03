import numpy as np
a=np.arange(1,31)
print(a)
a=a.reshape((6,5))
print(a)
print(a[2:4,0:2])
print("_________________________________")
for i in range(0,4):
    print(a[i,i+1])

print("_________________________________")
print(a[[0,4,5],3:])
