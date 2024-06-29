import numpy as np
def rotate_array(array,k):
    k=k%len(array);
    rotate=np.roll(array,k)
    return rotate.tolist()
array=[1,2,3,4,5]
print(rotate_array(array,2))