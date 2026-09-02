"""
Write a generator function called even_numbers that yields even numbers from 0 up
to (and including) a given limit n.
"""

def even_generator(n):
    i = 0
    while i <= n:
        yield i
        i += 2


print(list(even_generator(10)))
for x in even_generator(10):
    print(x)


def even_generator_lazy():
    i = 0
    while True:
        yield i
        i += 2

gen = even_generator_lazy()
print(list(next(gen) for _ in range(0, 12, 2)))

"""
Logged:

Generators/Iterators | Problem #1 (even_numbers generator) | Correct (first try,
plus self-driven bonus exploration of infinite generator) | Articulation: mostly clear,
one imprecise phrase on list memory model (self-corrected once clarified) | 
Referred: no | Insight: strong intuitive grasp of lazy vs eager evaluation trade-offs;
proactively explored beyond the ask, good sign of genuine curiosity/depth.
"""