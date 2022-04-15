import numpy as np
from scipy import linalg

a1, b1, a2, b2, c1, c2 = map(float, [input(), input(), input(), input(), input(), input()])
A = np.array([[a1, b1], [a2, b2]])
b = np.array([c1, c2])
x = linalg.solve(A, b)
print(x)

# if a1*b2 != a2*b1:
#     if a1 == 0:
#         y = c1/b1
#     if b1 == 0:
#         x = c1/a1
#     print(f"2 {x} {y}")

