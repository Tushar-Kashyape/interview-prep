from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter:

c = Counter("mississippi")
print(c, c.most_common(2), c["z"])

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2, c1 - c2)

# ==============================================================================

# defaultdict:

dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
print(dd)

dd_int = defaultdict(int)
words = ["a", "b", "a", "c", "b", "a"]
for word in words:
    dd_int[word] += 1
print(dd_int)

# gotcha: .get() does not trigger auto-creation, [] does.

dd2 = defaultdict(list)
print(dd2.get("missing"), "missing" in dd2)
print(dd2["missing"], "missing" in dd2)

# ==============================================================================

# deque:

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)
dq.pop()
dq.popleft()
print(dq)

# ==============================================================================

# namedtuple:

point = namedtuple("Point", ["x", "y"])
p = point(3, 4)
print(p.x, p.y)
print(p[0], p[1])
print(isinstance(p, tuple))
print(p)
# p.x = 10                      # AttributeError - immutable,like regular tuple

# ==============================================================================

# OrderedDict:

od1 = OrderedDict([("a", 1),  ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print(od1 == od2)

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)

# ==============================================================================

"""
Please visit, https://docs.python.org/3.14/library/collections.html for more info
and LRU cache implementation using OrderedDict
"""
