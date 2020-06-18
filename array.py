import array as arr
import random as rand

floats = arr('d', (rand() for i in range(10**7)))
print(floats[-1])