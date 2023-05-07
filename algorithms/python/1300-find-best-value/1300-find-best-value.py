def calc_sum(arr: list[int], value):
    return sum(value if num >= value else num for num in arr)


def find_bset_value(arr: list[int], target: int) -> int:
    # arr.sort()
    left = 0
    right = max(arr)

    while left < right - 1:
        mid = left + (right - left) // 2
        sum = calc_sum(arr, mid)

        if sum - target > 0:
            right = mid
        elif sum - target < 0:
            left = mid
        else:
            return mid

    left_dis = abs(calc_sum(arr, left) - target)
    right_dis = abs(calc_sum(arr, right) - target)
    if left_dis <= right_dis:
        return left
    else:
        return right


arr = [4, 9, 3]
print(find_bset_value(arr, 10))
