def dig_pow(n, p):
    digits = [int(i) for i in str(n)]
    the_sum = 0
    for power, num in enumerate(digits, start=p):
        the_sum = the_sum + (num ** power)

    return int(the_sum / n) if (the_sum / n).is_integer() else -1


# returns 2
print(dig_pow(695, 2))
# returns -1
print(dig_pow(132, 1))
