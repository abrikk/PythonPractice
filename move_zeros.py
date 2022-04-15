def move_zeros(array):
    new_array = [i for i in array if i != 0]
    new_array.extend(array.count(0) * [0])
    return new_array


print(move_zeros([0, 1, 9, 0, 0, 0, 0, 9]))

