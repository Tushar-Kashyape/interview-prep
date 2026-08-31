import functools

from sqlalchemy.util import decorator


# BASIC DECORATOR:

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returning {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(2, 3)

# returns wrapper if functools.wraps not used because wrapped by wrapper.
# returns add when functools.wraps(func) is used
print(add.__name__)

# ==============================================================================
# DECORATOR WITH ARGUMENTS (3 - layer nesting)

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"hi {name}")
    return name

greet("sam")

# ==============================================================================
# Stacked Decorators:

def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def exclaim(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

@shout
@exclaim
def say(msg):
    return msg

# exclaim runs first -> "hello!"
# "hello!" goes to shout -> HELLO!
print(say("hello"))

# ==============================================================================
# Real-world : memoization via lru_cache
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
