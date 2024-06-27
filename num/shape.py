import numpy as np

# create 1-d numpy array and get shape
np1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

# create 2-d array and get shape(rows/columns-elements)
# np2= np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2)
# print(np2.shape)

# reshape 2-d
# np3= np1.reshape(3,4)
# print(np3)
# print(np3.shape)

# reshape 3-d
np4= np1.reshape(2,3,2)
print(np4)
print(np4.shape)

# flatten to 1-d
np5= np4.reshape(-1)
print(np5)
print(np5.shape)