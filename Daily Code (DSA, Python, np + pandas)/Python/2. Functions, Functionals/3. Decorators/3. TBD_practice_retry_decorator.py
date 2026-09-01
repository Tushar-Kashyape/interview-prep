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
            retry_count = 1
            last_error = None

            while retry_count <= n:
                print(f"Attempt {retry_count}")
                try:
                    result = func(*args, **kwargs)
                    return result  # success — done, no more retries
                except ValueError as e:
                    last_error = e
                    retry_count += 1

            raise last_error
        return wrapper
    return dec


@retry(3)
def flaky():
    if random.random() < 0.5:
        raise ValueError("Failed...")
    return "Success!"