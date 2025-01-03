import numpy as np
#0 matrix of 1,2,3 d
a=np.zeros(5)
print(a)

b=np.zeros((2,3),dtype='int16')
print(b)

c=np.ones((3,2,4))
print(c)

d=np.full((3,4),100)
print(d)

e=np.full(c.shape,25,dtype="float32")
print(e)

f=np.random.rand(3,3)
#prints random decimal numbers between 0 to 1
print(f)
print()
g=np.random.random_sample(a.shape)
print(g)

#randint(start,stop,size)
h=np.random.randint(10,20,(4,3))
print(h)

i=np.identity(3)
print(i)

j=np.array([[1,2,3],[4,5,6]])
print(np.repeat(j,2,axis=0))
print(np.repeat(j,2,axis=1))

