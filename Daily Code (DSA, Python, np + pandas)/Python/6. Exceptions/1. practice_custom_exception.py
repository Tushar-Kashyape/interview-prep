"""
Write a custom exception InvalidAgeError that includes the invalid age as an attribute.
Write a function register_user(name, age) that raises InvalidAgeError if age is negative
or greater than 150, otherwise returns a success message. Catch the error at the call
site and print a message using the exception's attribute.
"""

class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Cannon register user, age {age} is invalid")
        self.age = age

def register_user(name, age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return f"{name} registered successfully "

try:
    register_user("Alice", 200)
except InvalidAgeError as e:
    print(f"Registration failed: age {e.age} is invalid")


print(register_user("Bob", 35))

"""
Logged:

Exceptions | Problem #1 (custom exception with attribute, InvalidAgeError) | 
Correct after 2 iterations (initial bugs: missing return vs print, tuple-formatting 
mistake in f-string, missing super().init) | Articulation: initial answer conflated 
message-setting mechanism with attribute-access mechanism, correctly self-corrected 
on follow-up once distinguished | Referred: no | Insight: solid understanding of custom 
exceptions overall; needed one nudge to cleanly separate "how the message works" from 
"how a custom attribute works" — both real but independent mechanisms, now clarified.
"""