""" Program which counts even digits in entered number. """
import string

num = input("Enter a number: ")
quantity = len([i for i in list([i for i in num if i in string.digits]) if float(i) in [2, 4, 6, 8]])
print(f"The quantity of even digits in number {num} is {quantity}")

