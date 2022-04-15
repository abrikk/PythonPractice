def rgb(r, g, b):
    rgbs = [r, g, b]
    for i, n in enumerate(rgbs):
        if n < 0:
            rgbs[i] = 0
        elif n > 255:
            rgbs[i] = 255

    return "".join(list([format(i, "X").zfill(2) for i in rgbs]))
