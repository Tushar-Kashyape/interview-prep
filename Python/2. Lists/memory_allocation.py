import sys
a = []
prev = sys.getsizeof(a)
for i in range(20):
    a.append(i)
    size = sys.getsizeof(a)
    if size != prev:
        print(f"len={len(a)}: size jumped to {size} bytes")
        prev = size