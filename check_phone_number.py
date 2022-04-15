import string


def make_num(num):
    num = "".join([i for i in num if i in string.digits])
    if len(num) == 7:
        num = "495" + num
    else:
        num = num[1:]
    return num


user_num = make_num(input())
numbers = make_num(input()), make_num(input()), make_num(input())
print(numbers)
for number in numbers:
    if number == user_num:
        print("YES")
    else:
        print("NO")
