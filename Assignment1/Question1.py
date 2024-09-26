# 1. Write a NumPy program to create an array with the values 1, 7, 13, 105  and
# determine the size of the memory occupied by the array.

import numpy as np

def funct():
    arr1=np.array([1,7,13, 105])
    print(f"Size of array = {arr1.nbytes}")
    print(f"size of the array = {arr1.itemsize*arr1.size}")

funct()