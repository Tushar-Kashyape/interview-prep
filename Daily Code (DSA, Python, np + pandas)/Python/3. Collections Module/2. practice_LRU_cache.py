"""
You're implementing a simple LRU (Least Recently Used) cache with a fixed capacity.
When the cache is full and a new item is added, the least recently used item should
be evicted. Accessing an existing key should mark it as "recently used" (moves it to
the end).

Use OrderedDict and its move_to_end() method.
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def get(self, key):
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key)
            return self.lru_cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.lru_cache:
            self.lru_cache[key] = value
            self.lru_cache.move_to_end(key)
        else:
            if len(self.lru_cache) == self.capacity:
                self.lru_cache.popitem(last=False)

            self.lru_cache[key] = value

cache = LRUCache(2)
cache.put(1, "a")
cache.put(2, "b")
print(cache.get(1))                 # "a" — 1 is now most recently used
cache.put(3, "c")         # capacity exceeded, evicts 2 (least recently used)
print(cache.get(2))                 # -1 — evicted
print(cache.get(3))                 # "c"

"""
Logged: 

collections | LRUCache (OrderedDict-based, checkpointed) | Correct across 
all 3 checkpoints, no bugs | Articulation: correct on redundant move_to_end catch, 
honest gap acknowledged on popitem(last=False) mechanics, resolved with explanation | 
Referred: no (checkpointing was a process choice, not a hint requirement) | 
Insight: good self-directed checkpointing discipline; correctly reasoned about 
redundancy without prompting; one genuine terminology/mechanism gap (why last=False -> 
front) cleanly closed.
"""