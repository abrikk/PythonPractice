def find_next_square(sq):
    return pow(pow(sq, 1 / 2) + 1, 2) if pow(sq, 1 / 2) % 1 == 0 else -1


# returns 144
print(find_next_square(121))
# returns -1
print(find_next_square(111))
