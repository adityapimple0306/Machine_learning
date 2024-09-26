# 3.  Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives,
# 10 tens, 10 twentys and 10 fiftys.
#
import numpy as np

a1 = np.zeros(10)
print(f"a1 = {a1}")

a2 = np.ones(10, dtype=np.int8)

print(f"a2 = {a2}")
print("-"*80)
a3 = a2*5
print(a3)
print("-"*80)
a4 = a3 *2
print(a4)
print("-"*80)
a5 = a2 *20
print(a5)
print("-"*80)
a6 = a2 *50
print(a6)
print("-"*80)