# Basic try/except/else/finally
from logging import log


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Cannot divide by zero:", e)
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Cleanup always runs")

print(divide(10, 2))
print(divide(10, 0))

# ==============================================================================

# Multiple Exception Types:

def parse(val):
    try:
        return int(val)
    except (TypeError, ValueError) as e:
        print(f"Bad Input: {e}")
        return None

print(parse("abc"))
print(parse(None))

# ==============================================================================

# Exception hierarchy - Catching broadly vs specifically:

try:
    d = {}
    print(d["missing_key"])
except LookupError as e:         # catches KeyError AND IndexError
    print("Lookup failed: ", type(e).__name__, e)

# ==============================================================================

# Ordering matters - Specific before General

def risky_ordering(x):
    try:
        return 10/ x
    except ZeroDivisionError as e:
        print(f"specific: {e}")
    except Exception:
        print(f"general: something else")
# if Exception came FIRST, ZeroDivisionError would never be reached
print(risky_ordering(0))

# ==============================================================================

# Custom Exception with Attributes:

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(e)
    print(e.balance, e.amount)

# ==============================================================================

# Exception Chaining:

class ConfigError(Exception):
    pass

def load_config():
    try:
        int("not_a_number")
    except ValueError as e:
        raise ConfigError("Failed to load configs") from e

try:
    load_config()
except ConfigError as e:
    print(e)
    print("Caused by: ",e.__cause__)
    print(type(e).__name__, type(e.__cause__).__name__)
    #       ConfigError             ValueError
# ==============================================================================

# Re-raising Exception:

def process():
    try:
        1 / 0
    except ZeroDivisionError:
        print("Logging the error...")
        raise

try:
    process()
except ZeroDivisionError:
    print("caught it again at caller level")

# ==============================================================================

# Custom Exception Hierarchy:

class AppError(Exception):
    pass
class ValidationError(AppError):
    pass
class DatabaseError(AppError):
    pass

def validate(x):
    if x < 0:
        raise ValidationError("x must be non-negative")

try:
    validate(-5)
except AppError as e:
    print("App level error", e)

# ==============================================================================