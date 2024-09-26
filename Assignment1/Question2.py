# 2. Write a NumPy program to create an element-wise comparison
# (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np

a1 = np.array([10,20,30,40,50])
a2 = np.array([10,20,30,40,50])

print(f"a1 > a2 = {a1 > a2}")
print(f"a1 >= a2 = {a1 >= a2}")
print(f"a1 < a2 = {a1 < a2}")
print(f"a1 <= a2 = {a1 <= a2}")