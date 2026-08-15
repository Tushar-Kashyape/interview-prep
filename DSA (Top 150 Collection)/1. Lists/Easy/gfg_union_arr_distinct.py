def find_union(a, b):
    return sorted(list(set(a + b)))

a = [89, 24, 75, 11, 23]
b = [89, 2, 4]
print(find_union(a, b))