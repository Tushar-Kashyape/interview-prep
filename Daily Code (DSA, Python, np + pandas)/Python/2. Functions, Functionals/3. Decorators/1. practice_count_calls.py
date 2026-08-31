"""
Write a decorator called count_calls that tracks how many times the decorated function
has been called, and prints that count each time the function runs.
"""
import functools


def count_calls(func):
    call_count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"Call #{call_count} to greet")
        result = func(*args, **kwargs)
        return result
    return wrapper

@count_calls
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
greet("Bob")

"""
Decorators | count_calls problem | Correct (2 iterations) 
| Articulation: clear, minor imprecision on nonlocal's exact role | Referred: no 
| Insight: understands closure persistence and mutation-vs-reassignment distinction well; 
initial miss was scope-of-declaration, self-corrected once flagged.
"""