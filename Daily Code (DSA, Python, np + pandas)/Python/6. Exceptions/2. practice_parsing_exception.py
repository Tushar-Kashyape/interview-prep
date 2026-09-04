"""
Write a function parse_and_double(value) that tries to convert value to an integer
and return double it. If conversion fails, catch the underlying error and raise a
custom exception ParsingError — which should have a message and store the original
invalid value as an attribute — chaining it from the original exception using from.
"""
class ParsingError(Exception):
    def __init__(self, value):
        super().__init__(f"Unable to parse {value}")
        self.value = value


def parse_and_double(value):
    try:
        return int(value) * 2
    except ValueError as e:
        raise ParsingError(value) from e

try:
    parse_and_double("abc")
except ParsingError as e:
    print(f"Failed to parse: {e}")
    print(f"Bad value was: {e.value}")
    print(f"Caused by: {e.__cause__}")
    print(type(e).__name__, type(e.__cause__).__name__)

print(parse_and_double("25"))

"""
Logged:

Exceptions | Problem #2 (ParsingError with chaining, message + attribute + cause) | 
Correct, first try, cold — successfully combined the previously-flagged gap (message 
vs attribute mechanisms) correctly this time, plus new chaining mechanics | 
Articulation: precise, correctly identified from as Python-level automatic behavior, 
not manual assignment | Referred: no | Insight: gap from Problem #2 (conflating 
message/attribute mechanisms) is now resolved — handled both cleanly together in 
this harder combined problem, confirming it was a one-time confusion, not a persistent 
misunderstanding.
"""