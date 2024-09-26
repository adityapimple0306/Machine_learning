import numpy as np


# 21. Write a NumPy program to convert a list array.

list1= [10,20,30,40,50,90]

def list_to_array(new_list):
    arr1 = np.array(new_list)

    return arr1

print(list_to_array(list1))
