square = lambda x: x * x
print(square(5))

# ==============================================================================

# key= for Sorting:

pairs = [(1, "z"), (3, "a"), (2, "m")]
print(sorted(pairs, key=lambda p: p[1]))
print(sorted(pairs, key=lambda p: p[0], reverse=True))

people = [("Bob", 25), ("Alice", 25), ("Zed", 20)]
# Sorting by age first, if same age then by name
print(sorted(people, key=lambda p: (p[1], p[0])))
print(max(people, key=lambda p:p[1]))

people = [
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 25},
    {"name": "Zed", "age": 20}
]
print(sorted(people, key=lambda d: (d["age"], d["name"])))

# If we want to sort one by descending and other by ascending then following ways:
# A:
print(sorted(people, key=lambda d: (-d["age"], d["name"])))
# B:
sort_step1 = sorted(people, key=lambda d: d["age"], reverse=True)
print(sorted(sort_step1, key=lambda d:d["name"]))

# ==============================================================================

larger = lambda a, b: a if a > b else b
print(larger(3, 8))

# ==============================================================================

# Closure over enclosing variable:

def make_multiplier(n):
    return lambda x: x * n

doubler = make_multiplier(2)
print(doubler(10))

# ==============================================================================

# Late Binding Gotcha:

funcs = [lambda: i for i in range(3)]
# [2, 2, 2] instead of [0, 1, 2]
print([func() for func in funcs])

funcs_fixed = [lambda i=i:i for i in range(3)]
print([func() for func in funcs_fixed])

"""
Late binding — crisp pointers:

. "Binding" = connecting a name to a value. "Late" = that connection happens at call 
time, not creation time.
. Closures capture the variable itself (a reference), not a snapshot of its value.
. Loop var i is one shared variable across all iterations — not a fresh i per iteration.
. Lambda body just says i → looked up when called, not when defined.
. After loop ends, i = last value (e.g. 2). All lambdas see that same final 
value → [2, 2, 2].
. Fix: lambda i=i: i — default arg values ARE evaluated at definition time, so this 
bakes in the current value immediately, creating an independent local i per lambda.
. Root cause: default-arg early evaluation vs. closure late evaluation — different 
timing rules for different mechanisms.
"""
# ==============================================================================

# filter/ map with lambda:

nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))
print(list(map(lambda x: x * 2, nums)))
print([x for x in nums if x % 2 == 0])

# ==============================================================================