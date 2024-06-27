import numpy as np

# copy vs. view
np1= np.array([0,1,2,3,4,5])

#create a view
# np2 = np1.view()

# print(f'original np1 {np1}')
# print(f'original np2 {np2}')

# np1[0]= 41
# print(f'changed np1 {np1}')
# print(f'original np2 {np2}')

# create a copy
np2=np1.view()
print(f'original np1 {np1}')
print(f'original np2 {np2}')

np2[0]= 41
print(f'changed np1 {np1}')
print(f'original np2 {np2}')
