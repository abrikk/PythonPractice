def is_isogram(string):
    return sorted(string.lower()) == sorted(set(string.lower()))


print(is_isogram("aba"))
print(is_isogram("Dermatoglyphics"))
