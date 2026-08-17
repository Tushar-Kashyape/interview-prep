from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)


s = "car"
t = "rat"
print(is_anagram(s, t))