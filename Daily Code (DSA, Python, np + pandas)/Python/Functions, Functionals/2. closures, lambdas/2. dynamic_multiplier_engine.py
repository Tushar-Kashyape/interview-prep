"""
Dynamic Multiplier Engine

Imagine you are building a pricing engine or tax calculator. You need a way to
generate custom transformation functions on the fly (e.g., double, triple, add_vat),
while also keeping track of how many times each generated function has been executed.

"""

"""
In 1. Stateful Event Counter, state was for dictionary which is mutable.
So, there wasn't need to use "nonlocal" :keyword, but here it is immutable integer
so we have used nonlocal to keep track of state.
"""


def make_multiplier(factor: float):
    """
    Custom multiplier function - uses factor by which to be multiplied
    User closure state to keep track of execution count - "nonlocal" keyword.
    """
    call_count = 0

    def multiplier(x: float) -> float:
        nonlocal call_count
        call_count += 1
        return x * factor

    multiplier.get_stats = lambda:(f"Applied factor {factor}x exactly {call_count} "
                                   f"time(s).")

    def reset():
        nonlocal call_count
        call_count = 0
        print("Reset done")

    multiplier.reset = reset

    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(5))
print(triple(20))

print(double.get_stats())
print(triple.get_stats())

triple.reset()
print(triple.get_stats())