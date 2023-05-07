def length_of_longest_substring1(s: str) -> int:
    n = len(s)
    if n < 2:
        return n

    freq = dict.fromkeys(s, 0)
    res = 1

    left = right = 0

    while right < n:
        freq[s[right]] += 1

        if freq[s[right]] == 2:
            while freq[s[right]] == 2:
                freq[s[left]] -= 1
                left += 1

        res = max(res, right - left + 1)

        right += 1

    return res

def length_of_longest_substring2(s: str) -> int:
    n = len(s)
    if n < 2:
        return n

    window = dict.fromkeys(s, -1)
    res = 1

    left = right = 0

    while right < n:
        print(f'before {window} {left} {right}')
        if window[s[right]] != -1:
            left = max(left, window[s[right]] + 1)

        window[s[right]] = right
        print(f'after {window} {left} {right}')
        res = max(res, right - left + 1)
        right += 1

    return res

def lengthOfLongestSubstring3(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[rk + 1])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    return ans


s = "abcabcbb"
print(length_of_longest_substring1(s))

s = "bbbbb"
print(length_of_longest_substring1(s))

s= "abcdefghefgdcg"
print(length_of_longest_substring2(s))

s = "abcabcbb"
print(length_of_longest_substring2(s))

s = "bbbbb"
print(length_of_longest_substring2(s))

s= "abcdefghefgdcg"
print(length_of_longest_substring2(s))

s= "abba"
print(length_of_longest_substring2(s))