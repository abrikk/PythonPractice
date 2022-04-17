# seven(times(five()))  return 35
# four(plus(nine()))  return 13
# eight(minus(three()))  return 5
# six(divided_by(two()))  return 3

def divided_by(number2):
    def wrap(number):
        return number // number2

    return wrap


def plus(number2):
    def wrap(number):
        return number + number2

    return wrap


def minus(number2):
    def wrap(number):
        return number - number2

    return wrap


def times(number2):
    def wrap(number):
        return number * number2

    return wrap


def zero(func=None):
    number = 0
    if func is None:
        return number
    else:
        return func(number)


def one(func=None):
    number = 1
    if func is None:
        return number
    else:
        return func(number)


def two(func=None):
    number = 2
    if func is None:
        return number
    else:
        return func(number)


def three(func=None):
    number = 3
    if func is None:
        return number
    else:
        return func(number)


def four(func=None):
    number = 4
    if func is None:
        return number
    else:
        return func(number)


def five(func=None):
    number = 5
    if func is None:
        return number
    else:
        return func(number)


def six(func=None):
    number = 6
    if func is None:
        return number
    else:
        return func(number)


def seven(func=None):
    number = 7
    if func is None:
        return number
    else:
        return func(number)


def eight(func=None):
    number = 8
    if func is None:
        return number
    else:
        return func(number)


def nine(func=None):
    number = 9
    if func is None:
        return number
    else:
        return func(number)
