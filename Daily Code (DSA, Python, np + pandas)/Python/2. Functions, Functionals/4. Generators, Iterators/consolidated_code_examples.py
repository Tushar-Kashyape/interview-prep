# ITERABLE vs ITERATOR:

lst = [1, 2, 3]
it = iter(lst)                          # lst was iterable; now iterator
print(next(it), next(it), next(it))     # 1 2 3
# next(it)                              Raises StopIteration

# ==============================================================================
# GENERATOR FUNCTION:

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)                    # Calling - not executing - starting
print(next(gen), next(gen), next(gen))  # 1 2 3 -lazy, one at a time
# next(gen)                             # Raises Exception

# ==============================================================================
# FOR LOOP USES [iter and next] -a contract of two methods protocol automatically:

for x in count_up_to(3):
    print(x)

# ==============================================================================
# GENERATOR EXPRESSION vs LIST COMPREHENSION:

gen_expr = (x*x for x in range(5))      # Lazy - no execution yet
list_comp = [x*x for x in range(5)]     # Eager - full computation done
list(gen_expr)                          # [0 1 4 9 16] - forces lazy to eager

# ==============================================================================
# yield PRESERVES STATE B/W CALLS:

def running_total():
    total = 0
    while True:
        x = yield total
        total += x

rt = running_total()                    # created generator obj
next(rt)                                # first call - yields total 0 - pause
rt.send(5)                              # x gets 5, total + x, yields 5 - pause
rt.send(10)                             # x gets 10, total + x, yields 15 - pause

# ==============================================================================
# yield FROM DELEGATION:

def inner():
    yield 1
    yield 2

def outer():
    yield from inner()
    yield 3

list(outer())                   # [1 2 3]

# ==============================================================================
# CLASS-BASED ITERATOR:

class Countup:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        print('  __iter__ called')
        return self

    def __next__(self):
        print(f'  __next__ called, self.i={self.i}')
        if self.i >= self.n:
            print('  raising StopIteration')
            raise StopIteration
        self.i += 1
        return self.i

print('starting for loop:')
for x in Countup(3):
    print('got value:', x)

# ==============================================================================
# INFINITE GENERATOR(only possible because of lazy)

def infinite_counter():
    i = 0
    while True:
        yield i
        i += 1

counter = infinite_counter()
# [0,1,2,3,4] — never tries to build the whole thing
print([next(counter) for _ in range(5)])
# ==============================================================================
