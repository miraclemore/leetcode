def time_cost(piles, speed):
    time = 0
    for pile in piles:
        time += (pile + speed - 1) // speed

    return time


def min_eating_speed(piles: list[int], h: int) -> int:
    speed_low = 1
    speed_high = max(piles)

    speed_ans = speed_high

    while speed_low < speed_high:
        speed_mid = speed_low + (speed_high - speed_low) // 2

        time = time_cost(piles, speed_mid)

        if time <= h:
            speed_high = speed_mid
            speed_ans = speed_mid
        elif time > h:
            speed_low = speed_mid + 1

    return speed_ans


piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))

piles = [30,11,23,4,20]
h = 5
print(min_eating_speed(piles, h))
