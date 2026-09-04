"""
To Be Done:

Write a decorator called retry that takes a number of attempts n and retries the
decorated function if it raises an exception, up to n total attempts. If all attempts
fail, re-raise the last exception. If it succeeds on any attempt, return the result
immediately (no further retries).
"""
import functools
import random


def retry(n):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= n:
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f"Attempt: {attempt}")
                    if attempt < n:
                        attempt += 1
                    else:
                        raise
            return None
        return wrapper
    return dec


@retry(3)
def flaky():
    if random.random() < 0.5:
        raise ValueError("Failed...")
    return "Success!"

"""
Logged:

Decorators+Exceptions | retry decorator (parked gap, closed) | Correct, first try this
time — clean unified loop, no special-cased first call | Articulation: mostly correct,
slightly imprecise framing ("no try except earlier" vs. the actual issue of inconsistent/
duplicated call paths) — clarified | Referred: no | Insight: genuine improvement from 
two days ago; correctly internalized "one uniform path for all attempts" as the fix, 
even if the exact framing of the original bug needed sharpening.
"""