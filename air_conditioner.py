troom, tcond = map(int, input().split())
mode = input()

if mode == "auto":
    print(tcond)
if mode == "fan":
    print(troom)
if mode == "freeze":
    if tcond < troom:
        print(tcond)
    else:
        print(troom)
if mode == "heat":
    if troom > tcond:
        print(troom)
    else:
        print(tcond)
