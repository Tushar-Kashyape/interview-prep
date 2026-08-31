"""
Write a decorator called memoize that caches a function's return value based on
its arguments — if the function is called again with the same arguments, return
the cached result instead of recomputing.
"""
import functools


def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

# @functools.lru_cache(maxsize=None)
@memoize
def slow_square(n):
    print(f"Computing square of {n}")
    return n * n

slow_square(4)
slow_square(4)
slow_square(5)

"""
Logged: Decorators | memoize problem | Correct (near first-try, one trivial syntax fix) 
| Articulation: correct on hashability, initial miss on closure-independence reasoning 
(said "call stacks," actual mechanism is per-invocation closure) — self-corrected after 
explanation | Referred: no | Insight: solid on decorator mechanics and caching logic; 

slight fuzziness on distinguishing closures from call-stack/runtime concepts, 
worth reinforcing.
"""
