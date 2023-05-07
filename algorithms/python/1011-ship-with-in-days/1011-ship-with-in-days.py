def check(weights: list[int], w):
    day = 1
    total = 0
    for weight in weights:
        if total + weight > w:
            total = 0
            day += 1
        total += weight
    return day


def ship_with_in_days(weights: list[int], days: int) -> int:
    low = max(weights)
    high = sum(weights)

    while low < high:
        mid = low + (high - low) // 2

        if check(weights, mid) > days:
            low = mid + 1
        else:
            high = mid

    return high


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(ship_with_in_days(weights, days))

weights = [3, 2, 2, 4, 1, 4]
days = 3
print(ship_with_in_days(weights, days))

weights = [1, 2, 3, 1, 1]
days = 4
print(ship_with_in_days(weights, days))
