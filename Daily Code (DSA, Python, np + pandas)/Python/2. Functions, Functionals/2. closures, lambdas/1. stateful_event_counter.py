"""
Write a function create_event_counter(initial_counts=None) that uses closures and
lambdas to implement a light stateful counter engine without using any classes or
global variables.

Imagine you are building a logging or analytics tool for a website. You need to
count how many times different events happen—like clicks, page views, or purchases.

Normally, you want to be able to do three things:

1) Log an event: "Add 1 to click" or "Add 5 to view".

2) Get the total: "How many total actions happened across all events?"

3) Reset: "Reset the click count to 0" or "Clear all counts."
"""
def create_event_counter(initial_counts=None):
    """
    Creates a stateful counter engine using closures and function attributes.
    Maintains encapsulated state without using classes or global variables.
    """
    if initial_counts is None:
        state = {}
    else:
        state = dict(initial_counts)


    def count_events(event: str, incr: int=1) -> dict:
        state[event] = state.get(event, 0) + incr
        return state

    count_events.get_total = lambda: sum(state.values())

    def reset(event=None):
        if event is None:
            state.clear()
        else:
            state[event] = 0

    count_events.reset = reset

    return count_events

counter = create_event_counter({"click": 10})

events = input("Enter event/s: ").split()
for event in events:
    print(counter(event))

print("Total events: ",counter.get_total())

counter.reset("click")

print("Clicks after reset:", counter("click"))
print("Total events:", counter.get_total())

counter.reset()
print("Total after full reset:", counter.get_total())

"""
I/p:

click click view click click

O/p:

{'click': 11}
{'click': 12}
{'click': 12, 'view': 1}
{'click': 13, 'view': 1}
{'click': 14, 'view': 1}
Total events:  15
Clicks after reset: {'click': 1, 'view': 1}
Total events: 2
Total after full reset: 0
"""