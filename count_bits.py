def count_bits(n):
    return sum(map(int, list(bin(n))[2:]))


# returns 3
print(count_bits(22))
# returns 16
print(count_bits(123456789))
