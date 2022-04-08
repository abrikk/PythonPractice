""" Finding the sum of sequences 0.5 + 1.5 + 2.5 + ... + 98.5 + 99.5 using Python."""

# The simplest first way in one line
print("The sum is: ", sum([i-0.5 for i in range(1, 101)]))

# The second way
sum_of_nums = 0
for num in range(1, 101):
    sum_of_nums = sum_of_nums+(num-0.5)
print("The sum is: ", sum_of_nums)

# The third way using external function arange in Numpy library
import numpy as np

sum_x = 0
for i in np.arange(0.5, 100.5, 1):
    sum_x += i

print("The sum is: ", int(sum_of_nums))

