def solution(number):
    nums = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)

    return sum(nums)

    # the shortes way
    # return sum([i for i in range(1, number) if i % 3 ==0 or i % 5 == 0])

