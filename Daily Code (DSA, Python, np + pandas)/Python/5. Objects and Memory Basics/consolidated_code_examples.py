## PYTHON OBJECT & MEMORY Basics:

import copy
import sys
import gc

# Object Refs.

a = [1, 2, 3]
b = a                           # b is a REFERENCE to the same object, not a copy
b.append(4)
c = a + [5]
print(c)
print(a)                        # a sees changes too

# ==============================================================================

# is vs. ==

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)   # True
print(x is y)   # False
print(x is x)   # True

# ==============================================================================

# Mutable vs Immutable:

s = "Hello"
t = s + " World"
print(s, t)
lst = [1, 2, 3]
lst.append(4)
print(lst)

# ==============================================================================

# Shallow copy vs Deep Copy:

nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow.append([5, 6])
shallow[0].append(99)               # new OUTER list, but inner lists still SHARED
print(nested)                       # [[1, 2, 99], [3, 4]]

deep = copy.deepcopy(nested)
deep[0].append(100)
print(nested)                        # [[1, 2, 99], [3, 4]]

# ==============================================================================

# __eq__ without __hash__ = unhashable

class PointNoHash:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = PointNoHash(1, 2)
p2 = PointNoHash(1, 2)
print(p1 == p2)                 # True — custom equality works

try:
    {p1, p2}
except TypeError as e:
    print("Error: ", e)         # Error:  unhashable type: 'PointNoHash'


# Correct: __eq__ AND __hash__ together

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p3 = Point(1, 2)
p4 = Point(1, 2)
print(p3 == p4)
print({p3, p4})
print(len({p3, p4}))

# ==============================================================================

# GC: Reference counting basics

a =[1, 2, 3]
print(sys.getrefcount(a))   # baseline count (includes the temporary ref from the
                            # call itself)
b = a
print(sys.getrefcount(a))   # count increased by 1
del b
print(sys.getrefcount(a))   # count decreased back

# ==============================================================================

# Cyclic references — reference counting alone can't clean these up

class Node:
    def __init__(self):
        self.other = None

n1 = Node()
n2 = Node()
n1.other = n2                   # n1 references n2
n2.other = n1                   # n2 references n1 - cycle

del n1
del n2

# both names gone, but they still reference EACH OTHER
# they are now unreachable garbage, but ref count never hit 0 naturally
# Python's cyclic GC (gc module) will eventually clean this up automatically

print(gc.collect())             # manually trigger collection, returns count of
                                # objects collected

