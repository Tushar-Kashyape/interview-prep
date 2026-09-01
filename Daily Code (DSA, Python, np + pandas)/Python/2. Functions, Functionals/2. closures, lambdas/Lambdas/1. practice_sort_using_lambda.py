"""
Given a list of tuples representing students (name, score), sort the list by score
in descending order using a lambda as the sort key.

Expected output — sorted by score descending, ties keep original relative order
(stable sort):
"""
students = [("Alice", 82), ("Bob", 91), ("Charlie", 75), ("Dave", 91)]
print(sorted(students, key=lambda s: s[1], reverse=True))

"""
Log:

Lambdas | Problem #1 (sort students by score desc) | Correct (first try) | 
Articulation: shaky — conflated sort stability with "explicit key only applies 
to itself," then guessed alphabetical reasoning for unstable case which doesn't 
apply since name isn't in the key at all | Referred: no | 
Insight: solid on lambda/key mechanics, needs to internalize "stability" as a 
distinct, separate guarantee from sort direction — not derived from the key logic 
itself.

Key Pointers:

Sort stability — crisp pointers:

. Stability = a separate guarantee from sort direction (reverse=True/False) — two 
different concepts.
. Definition: if two elements compare equal on the sort key, a stable sort never 
changes their relative order from the input.
. reverse=True reverses overall direction, but does not touch how ties are handled 
— ties still preserve original relative order either way.
. Python's sorted()/.sort() uses Timsort, which is guaranteed stable — documented 
behavior, not coincidence.
. Why it matters: enables reliable multi-pass sorts (sort by least-priority key 
first, then higher-priority key next, relying on stability to preserve earlier 
ordering within ties).
. If a sort is NOT stable: order of tied elements becomes undefined/unpredictable 
— no way to guess it, since instability means zero guarantee on tie order.
. Key point: stability is about the algorithm's guarantee, not something derived 
from what fields happen to be in your key= lambda.
"""