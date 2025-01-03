import numpy as np


#0 - vertical
#1 - horizontal
stats=np.array([[1,4,3],[4,2,6]])
print(stats)
min=np.min(stats)
max=np.max(stats)
print(min)
print(max)
print(np.min(stats,axis=0))
print(np.min(stats,axis=1))

sum=np.sum(stats)
print(sum)

avg=np.mean(stats)
print(avg)