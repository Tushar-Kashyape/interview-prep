"""
Write a generator function called fibonacci that yields Fibonacci numbers infinitely
(no upper limit — this generator should never run out of values on its own).
"""

def fibonacci():
    i = 0
    j = 1
    while True:
        yield i
        i, j = j, i + j


fib = fibonacci()
first_10 = list(next(fib) for _ in range(10))
print(first_10)

"""
Logged:

Generators/Iterators | Problem #2 (infinite fibonacci generator) | Correct after 
guided derivation (needed step-by-step breakdown to get started, then self-corrected 
to idiomatic tuple-swap) | Articulation: correct core idea, needed slight precision 
tightening | Referred: yes — required scaffolding to begin (not fully cold) | 
Insight: understands the mechanics once shown the pattern, but didn't independently 
recall the "two-variable running total" technique from first principles; worth flagging 
as needing more repetition on this specific pattern (running-sum/sliding-window state 
machines) rather than generators themselves.
"""