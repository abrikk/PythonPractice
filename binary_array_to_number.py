def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


# returns 22
print(binary_array_to_number([1, 0, 1, 1, 0]))
# returns 1
print(binary_array_to_number([0, 0, 0, 1]))
