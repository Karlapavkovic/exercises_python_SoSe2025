import numpy as np
import math 
x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
x_log = []
for a in x:
    x_log.append((math.log10(a)))
 
print(x_log)

c = np.log10(x)
print(c)    

