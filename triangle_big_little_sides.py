p = int(input())
a = p // 3
b = (p - a) // 2
c = p - a - b
if a + b <= c:
    print(-1)
else:
    print(a, b, c)
    if p % 2 == 1:
        d = 1
    else:
        d = 2
    e = (p - d) // 2
    f = p - d - e
    print(d, e, f)
