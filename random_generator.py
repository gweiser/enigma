import random

def generator(length):
    nums = []
    while len(nums) < length:
        num = random.randint(1, length)
        if num not in nums:
            nums.append(num)

    return nums

def main():
    nums = generator(26)
    print(nums)


main()