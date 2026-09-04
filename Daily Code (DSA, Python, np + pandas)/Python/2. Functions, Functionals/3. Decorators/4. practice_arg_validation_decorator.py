"""
Write a decorator called validate_positive that checks all positional arguments
are positive numbers before calling the function; if any argument is ≤ 0, print
"Invalid input" and return None instead of calling the function (no exceptions
needed — just an if check).
"""
import functools

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Came up during follow-up Qs asked by AI-agent
        for val in list(args) + list(kwargs.values()):

            if type(val) not in (int, float) or val <= 0:
                print(f"Invalid inputs {args, kwargs}")
                return None

        return func(*args, **kwargs)
    return wrapper


@validate_positive
def compute(a, b):
    return a + b

print(compute(3, 5))
print(compute(-6, 8))


"""
Log:
Decorators | validate_positive problem | Correct (first try) 
| Articulation: mostly clear — correct on kwargs gap, slightly imprecise on cross-type 
comparison behavior (guessed lexicographic instead of TypeError) | Referred: no 
| Insight: solid grasp of *args/**kwargs distinction and decorator mechanics; minor 
gap on Python 3's strict type-comparison rules — worth a quick note, not a deep dive.


Final Log:
Decorators | validate_positive (with follow-up refinements) | Correct, self-driven 
iteration | Referred: no | Insight: good instinct to proactively apply feedback without 
being asked again.
"""