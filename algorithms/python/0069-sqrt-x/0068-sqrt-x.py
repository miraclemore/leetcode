def my_sqrt(x: int) -> int:
    i = 0

    if 0 <= x <= 1:
        return x

    if x == 2 or x == 3:
        return 1

    low = 2
    high = int(x / 2)

    mid = 0
    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid > x:
            high = mid - 1
        elif mid * mid < x:
            ans = mid
            low = mid + 1
        else:
            return mid

    return ans


print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(6))