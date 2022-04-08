""" Program which prints all divisors of natural numbers. """
num = int(input("Enter a natural number: "))
all_divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        all_divisors.append(str(i))

print(f"The all divisors of {num}: {', '.join(all_divisors)}")
