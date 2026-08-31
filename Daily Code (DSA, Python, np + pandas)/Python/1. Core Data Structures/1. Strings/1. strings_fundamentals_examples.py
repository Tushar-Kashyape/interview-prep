import time

s = "hello"
s2 = s
s += " world"
# print(s)

"""
Theory: Never build large strings with += in a loop; always join.
"""
bad = ""
start_time = time.perf_counter()
for c in "a" * 10000:
    bad += c
end_time = time.perf_counter()
# print(end_time - start_time)

start_time = time.perf_counter()
good = ("b" * 10000).join(c for c in "abcde")
end_time = time.perf_counter()
# print(end_time - start_time)

# ==============================================================================
print("  a  b  c  ".split())
# ['a', 'b', 'c']
print("  a  b  c  ".split(" "))
# ['', '', 'a', '', 'b', '', 'c', '', '']
print("xxxabcxxx".strip("x"))
# abc

# ==============================================================================
print("file.py".endswith((".py", ".txt")))
# ==============================================================================
table = str.maketrans("abc", "xyz")
print("aabbcc".translate(table))
# ==============================================================================
freq = [0]*26
for c in "aabbbc":
    freq[ord(c) - ord("a")] += 1
print(freq)
# ==============================================================================
b = "hello".encode("utf-8")
print(b)
print(b.decode("utf-8"))
# ==============================================================================

