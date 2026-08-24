"""
Write a function track_events that serves as a global logging middleware. It must
accept a mandatory string event_name, an arbitrary sequence of positional details,
and an arbitrary group of keyword metadata tags.The function should serialize the
input into a structured dictionary. Crucially, enforce that the keyword tags can
only accept keys that are explicitly defined in an active whitelist: {"status", "user_id", "source"}.
If an un-whitelisted keyword parameter is passed, raise a ValueError.

str: event_name
*args: details of type str
**kwargs: group of keyword - metadata tags
"""

"""
Got this problem by directly searching on Google. Classic problem.
Instead of providing in-place inputs tried to get mandatory input and positional
arguments (*args) from user. **kwargs also can be accepted from user.

args = input().split()
f(*args, **kwargs)
"""

def track_events(event_name: str, *details, **metadata_tags) -> dict:
    whitelist = {"status", "user_id", "source"}
    invalid_keys = metadata_tags.keys() - whitelist

    if invalid_keys:
        raise ValueError(f"Unwhitelisted keys provided: {invalid_keys}")

    return {
        "event": event_name,
        "details": list(details),
        "tags": metadata_tags
    }

event_name = input("Event: ")
details = input("Enter positional details: ").split()

try:
    print(track_events(event_name, *details, user_id="user_99",
                       status="success", cookie="abcd6789"))
except ValueError as e:
    print(e)