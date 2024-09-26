
# 12. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
import numpy as np


a1 = np.random.randint(10,21,12)
print(a1.reshape(3,4))