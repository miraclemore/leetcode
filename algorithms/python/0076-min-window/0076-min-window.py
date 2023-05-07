def min_window(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    n = len(s)

    window = dict.fromkeys(s, 0)
    pattern = dict.fromkeys(t, 0)

    for tmp in t:
        pattern[tmp] += 1
    print(pattern)

    left = right = 0
    match = 0
    count = len(pattern)
    print('count=', count)
    min_len = n + 1
    start = 0

    while right < n:
        print("before", s[left:right])
        cur_char = s[right]
        if cur_char in pattern:
            window[cur_char] += 1

            if window[cur_char] == pattern[cur_char]:
                match += 1

        right += 1

        while count == match:
            print("after", s[left:right])
            if right - left < min_len:
                start = left
                min_len = right -left

            left_char = s[left]
            if left_char in pattern:
                window[left_char] -= 1

                if window[left_char] < pattern[left_char]:
                    match -= 1

            left += 1

    # print("The final str", start, min_len)
    if min_len == n + 1:
        return ""

    return s[start:(start + min_len)]


# s = "ADOBECODEBANC"
# t = "ABC"
# print(min_window(s, t))
#
# s = "aa"
# t = "aa"
# print(min_window(s, t))

s = "cabwefgewcwaefgcf"
t = "cae"
print(min_window(s, t))
