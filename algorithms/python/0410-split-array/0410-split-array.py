def check(nums: list[int], value):
    total = 0
    cnt = 1

    for n in nums:
        if total + n > value:
            total = 0
            cnt += 1
        total += n
    print(f'cnt = {cnt}')
    return cnt


def split_array(nums: list[int], k: int) -> int:
    left = max(nums)
    right = sum(nums)
    ans = 0

    print(f'left={left} right={right}')

    while left < right:
        mid = left + (right - left) // 2

        print(f'check {mid} left={left} right={right}')
        if check(nums, mid) > k:
            left = mid + 1
        else:
            right = mid

    return right


nums = [7, 2, 5, 10, 8]
m = 2
print(split_array(nums, m))

nums = [1, 2, 3, 4, 5]
m = 1
print(split_array(nums, m))

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(split_array(weights, days))

weights = [3,2,2,4,1,4]
days = 3
print(split_array(weights, days))