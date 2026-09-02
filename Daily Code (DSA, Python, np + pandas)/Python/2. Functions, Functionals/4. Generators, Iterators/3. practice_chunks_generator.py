"""
Write a generator function called chunked that takes a list and a chunk size n,
and yields successive chunks (as lists) of size n from the input list. The last
chunk may be smaller if the list doesn't divide evenly.
"""

def chunked(lst: list[int], n: int):
    i = 0
    length = len(lst)
    while i < length:
        yield lst[i: i + n]
        i += n

data = list(map(int, input("Enter the list: ").split()))
n = int(input("Enter n (less than length of data): "))
for chunk in chunked(data, n):
    print(chunk)

print(list(chunked(data, n)))

"""
Logged:

Generators/Iterators | Problem #3 (chunked generator, list-slicing based) | 
Correct on first try, solved fully cold, no hints needed | Articulation: excellent — 
precise on indexing-vs-slicing distinction (IndexError vs silent clamping), honest 
and accurate self-assessment when questioned further | Referred: no | 
Insight: pushed unprompted into a genuinely senior-level follow-up questioning whether 
his own solution was actually "optimized" — correctly identified that slicing still 
requires the full input list in memory upfront despite lazy output, then correctly 
derived (with guidance) that true memory efficiency requires the entire pipeline 
(source included) to be lazy, not just the one function in the middle; 
strong critical/self-evaluative instinct beyond just getting the answer right.
"""