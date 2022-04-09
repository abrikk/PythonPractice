def high_and_low(numbers):
    numbers = f"{max(map(int, numbers.split()))} {min(map(int, numbers.split()))}"
    return numbers


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
