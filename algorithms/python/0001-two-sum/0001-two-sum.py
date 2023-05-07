def two_sum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    d = dict()

    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum2(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    d = dict()

    for i in range(n):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [j, i]


def two_sum3(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    hashtable = dict()

    for i, v in enumerate(nums):
        if target - v in hashtable:
            return [hashtable[target - v], i]
        else:
            hashtable[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
print(two_sum2(nums, target))
print(two_sum3(nums, target))
