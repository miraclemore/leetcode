def find_duplicate(nums: list[int]) -> int:
    while nums[0] != nums[nums[0]]:
        temp = nums[0]
        nums[0] = nums[nums[0]]
        nums[temp] = temp
    return nums[nums[0]]


nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums))


def find_duplicate(nums: list[int]) -> int:
    low = 1
    high = len(nums) - 1

    while low < high:
        count = 0
        mid = low + (high - low) // 2

        for n in nums:
            if n <= mid:
                count += 1

        if count > mid:
            high = mid
            ans = mid
        else:
            low = mid + 1

    return low


nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))
