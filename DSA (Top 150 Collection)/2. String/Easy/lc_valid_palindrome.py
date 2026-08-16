def is_palindrome(s):
    s = "".join(s.lower().split())
    alnum_s = ""

    for c in s:
        if c.isalnum(): alnum_s += c

    return alnum_s == alnum_s[::-1]

s = ".,"
print(is_palindrome(s))