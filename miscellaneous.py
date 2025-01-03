import numpy as np
#loading a file 

data=np.genfromtxt('data.txt',delimiter=",")
print(data)
data=data.astype('int16')
print("____________________________________________________________________")
print(data)


#BOOLEAN MASKING AND ADVANCED INDEXING
print("____________________________________________________________________")

print(data>100)

print("____________________________________________________________________")

print(data[data> 100])

#indexing using lists 
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])
#above prints the values of the indexes 1 2 ans 8

print("____________________________________________________________________")


print(np.any(data >100 , axis=0))
print(np.any(data >100 , axis=1))
print((data > 50) & (data < 500))


