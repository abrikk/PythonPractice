def get_middle(s):
    if len(s) % 2 == 0:
        letters = s[int(len(s) / 2 - 1):int(len(s) / 2 + 1)]
    else:
        letters = s[len(s) // 2]
    return letters


# returns th
print(get_middle("python"))
# returns S
print(get_middle("TESLA"))
