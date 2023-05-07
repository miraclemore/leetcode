def check(bloomDay: list[int], days, m, k) -> bool:
    flowers = 0
    flowers_set = 0
    for bloom in bloomDay:
        if bloom <= days:
            flowers += 1
            if flowers == k:
                flowers_set += 1
                if flowers_set == m:
                    break
                flowers = 0
        else:
            flowers = 0

    return flowers_set == m


def min_days(bloomDay: list[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1

    low, high = min(bloomDay), max(bloomDay)

    while low < high:
        mid = low + (high - low) // 2

        if check(bloomDay, mid, m, k):
            high = mid
        else:
            low = mid + 1

    return high


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(min_days(bloomDay, m, k))

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 2
print(min_days(bloomDay, m, k))

bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(min_days(bloomDay, m, k))
