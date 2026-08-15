from collections import Counter

def first_unique_char(s):
    char_counts = Counter(s)
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1

s = "aaabbb"
print(first_unique_char(s))