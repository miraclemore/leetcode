def check(time: list[int], T: int, m) -> bool:
    total = 0
    day = 1
    i = 0
    xiaoyang = True
    xiaoyang_time = 0
    while i < len(time):
        xiaoyang_time = max(xiaoyang_time, time[i])
        if total + time[i] > T:
            if xiaoyang:
                xiaoyang = False
                total += time[i] - xiaoyang_time
                i += 1
            else:
                day += 1
                total = 0
                xiaoyang_time = 0
                xiaoyang = True
        else:
            total += time[i]
            i += 1

    return day <= m


def min_time(time: list[int], m: int) -> int:
    low = 0
    high = sum(time)

    while low < high:
        mid = low + (high - low) // 2

        if check(time, mid, m):
            high = mid
        else:
            low = mid + 1

    return high


time = [1, 2, 3, 3]
m = 2
print(min_time(time, m))

time = [999, 999, 999]
m = 4
print(min_time(time, m))

time = [82, 35, 6, 53, 37, 75, 69, 69, 53, 18]
m = 4
print(min_time(time, m))
