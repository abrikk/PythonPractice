a, b, c = map(int, [input(), input(), input()])

if c < 0:
    print("NO SOLUTION")
elif a == 0 and b == c ** 2:
    print("MANY SOLUTIONS")
else:
    if a != 0 and ((pow(c, 2) - b) / a).is_integer():
        print((pow(c, 2) - b) // a)
    else:
        print("NO SOLUTION")
