import numpy as np

sum_x = 0
for i in np.arange(0.5, 100.5, 1):
    print(i)
    sum_x += i
    print(sum_x)

print(int(sum_x))
