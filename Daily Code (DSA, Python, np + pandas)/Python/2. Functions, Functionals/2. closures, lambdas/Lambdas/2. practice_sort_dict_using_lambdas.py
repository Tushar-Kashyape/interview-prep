"""
You have a list of dictionaries representing products. Sort them by price ascending,
but products that are "out_of_stock": True should always appear after all in-stock
products, regardless of price.

Use a single sorted() call with one lambda as the key (hint: think about what a
boolean evaluates to numerically, and how tuple-key sorting handles multiple
priorities).
"""
products = [
    {"name": "A", "price": 50, "out_of_stock": False},
    {"name": "B", "price": 20, "out_of_stock": True},
    {"name": "C", "price": 30, "out_of_stock": False},
    {"name": "D", "price": 10, "out_of_stock": True},
]

print(sorted(products, key=lambda p: (p["out_of_stock"], p["price"])))

# O/p:
#
# [
#     {"name": "C", "price": 30, "out_of_stock": False},
#     {"name": "A", "price": 50, "out_of_stock": False},
#     {"name": "D", "price": 10, "out_of_stock": True},
#     {"name": "B", "price": 20, "out_of_stock": True},
# ]

"""
Log:

Lambdas | Problem #2 (sort with boolean priority key) | Correct (first try) |
Articulation: mostly clear, one terminology slip (said "hashed" instead of "int 
subclass/numeric comparison") | Referred: no | Insight: strong grasp of tuple-key 
priority ordering and its failure modes; good self-correction depth on the 
string-coincidence follow-up.

Boolean-as-sort-key — crisp pointers:

. bool is a subclass of int in Python: False == 0, True == 1 — direct numeric 
comparison, not hashing.
. Tuple key (bool_field, other_field) → sorts False group before True group first, 
then breaks ties using other_field.
. This is deliberate semantic guarantee, not coincidence — always reliable.
. Contrast: using strings like "yes"/"no" or "true"/"false" instead of real 
booleans → ordering depends on lexicographic accident, not guaranteed logic. 
E.g. "false" < "true" (f<t) would wrongly put false-labeled items first if intent 
was reversed — fragile, avoid.
. Tuple key order = priority order — first element = primary sort criterion, later 
elements = tiebreakers only.
. Swapping tuple field order changes priority entirely — e.g. (price, bool_field) 
sorts by price globally, ignoring the intended grouping.
"""


