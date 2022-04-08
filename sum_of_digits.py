""" Program which calculates the sum of digits of the entered number. """
import string

num = input("Enter a number: ")
sum_of_digits = sum([float(d) for d in list(num) if d in string.digits])
print(int(sum_of_digits))
