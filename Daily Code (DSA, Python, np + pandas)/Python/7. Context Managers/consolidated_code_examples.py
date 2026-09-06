# Class-based Context Manager:

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self                 # bound to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Time elapsed: {elapsed:.4f}s")
        return False                 # False/None = don't suppress exceptions

with Timer() as t:
    total = sum(range(1000000))
print(total)

# ==============================================================================

# Exception Suppression via __exit__'s return value:

class SuppressErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Suppressed: {exc_type.__name__}: {exc_val}")
        return True              # True = SWALLOW the exception, don't propagate

with SuppressErrors():
    raise ValueError("This won't crash the program")
print("Execution continues here")   # reached, because exception was suppressed

# ==============================================================================

# "with" -> Sugar for try/ finally, under the hood:

class Resource:
    def __enter__(self):
        print("Acquiring Resources")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing Resources")    # ALWAYS runs, exception or not
        return False
try:
    with Resource():
        raise RuntimeError("boom")
except RuntimeError as e:
    print(f"Caught after cleanup: {e}")

# ==============================================================================

# manual try/except/finally vs context manager doing the SAME thing

def manual_version():
    print("Acquiring resource (manual)")
    try:
        raise RuntimeError("boom")
    except RuntimeError as e:
        print(f"Caught: {e}")
    finally:
        print("Releasing resource (manual)")

manual_version()

class ResourceWithSuppression:
    def __enter__(self):
        print("Acquiring resources (Context Manager)")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resources (Context Manager)")
        return True             # suppress the exception — same effect as the except
                                # block above

with ResourceWithSuppression():
    raise RuntimeError("boom")

print("Continues here — exception was suppressed by __exit__")
# Mapping: __enter__ = setup before try. with-body = try.
# __exit__'s exception logic = except. __exit__ running unconditionally = finally.

# ==============================================================================

# contextlib.contextmanager — generator-based, less boilerplate writing a full class

from contextlib import contextmanager
import time

@contextmanager
def timer_context_mgr():
    start = time.time()
    yield                       # code before yield = __enter__, after = __exit__
    print(f"Elapsed: {time.time() - start:.4f}s")

with timer_context_mgr():
    total = sum(range(1000000))

# ==============================================================================

# contextlib with exception handling:

@contextmanager
def suppress_errors_cm():
    try:
        yield
    except ValueError as e:
        print(f"Suppressed: {e}")

with suppress_errors_cm():
    raise ValueError("also won't crash")

print("Continues here too")

# ==============================================================================