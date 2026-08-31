"""
Let's look at why these two decorators exists:

@classmethod (cls): Works with the Class itself, not a specific instance.
Used as an Alternative Constructor (Factory) to create objects from raw formats
(like CSV strings, dictionary payloads, or databases).

@staticmethod: Takes neither self nor cls. It is a Pure Utility Function that lives
inside the class simply because it is logically related.

================================================================================
Quick Learning Pointers for @classmethod & @staticmethod
@classmethod (cls):
-------------------
Primary Role: Acts on the Class itself, not individual instances.

First Parameter: cls (refers to the class object, passed automatically by Python).

Key Use Case 1 (Factory Constructors): Creates instances from alternate data formats
(from_csv(), from_json(), from_dict()).

Key Use Case 2 (Global Class State): Modifies class-level attributes shared across
all instances (e.g., global tax rate, total room counters).

Inheritance Advantage: Calling cls(...) inside a classmethod returns an instance
of the child class if invoked from a child class (Polymorphic creation).
-------------------------------------------------------------------------------
@staticmethod:

Primary Role: Acts as a standalone utility function attached to the class namespace.

First Parameter: None (does not take self or cls).

Key Use Case: Pure helper logic that does not read or modify instance or class state
(e.g., is_valid_type(), sanitize_string()).

Namespace Benefit: Keeps code clean by grouping utility logic under the class name
(Room.is_valid_type(...)) instead of cluttering your script with loose global functions.

================================================================================
Do I need to access instance attributes (self.price)?
   └─► YES: Use standard Instance Method

Do I need to create a new object instance or modify class-level variables?
   └─► YES: Use @classmethod (cls)

Do I just need a pure utility function that depends on NO object/class state?
   └─► YES: Use @staticmethod
"""

class Room:
    VALID_TYPES = {"STANDARD", "DELUXE", "SUITE"}

    def __init__(self, room_number: str, price_per_night: float,
                 room_type: str = "STANDARD"):
        self.room_number = room_number
        self.price_per_night = float(price_per_night)
        self.room_type = str(room_type).upper()

    def __repr__(self) -> str:
        return f"Room({self.room_number}, {self.price_per_night}, {self.room_type})"

    @classmethod
    def from_csv_string(cls, raw_csv: str) -> "Room":
        """
        Parses single string payload into a room instance.
        Example string: "101,2300.86,DELUXE"
        """
        parts = str(raw_csv).split(",")
        room_num = parts[0].strip()
        price = float(parts[1].strip())
        room_type = parts[2].strip() if len(parts) > 2 else "STANDARD"

        # cls -> Room, can be used for instantiation
        return cls(room_number=room_num, price_per_night=price, room_type=room_type)

    @staticmethod
    def is_valid_type(room_type: str) -> bool:
        return room_type.strip().upper() in Room.VALID_TYPES

input_room_type = input("Enter room type (e.g. STANDARD, DELUXE, SUITE): ")

if Room.is_valid_type(input_room_type):
    print(f"'{input_room_type}' is valid! ")
else:
    print(f"'{input_room_type}' is invalid. Allowed types: {Room.VALID_TYPES}")

raw_input = input("Enter data in (format: room_num, price, type): ")

room = Room.from_csv_string(raw_csv=raw_input)

print("\nSuccessfully instantiated Room object via @classmethod:")
print(repr(room))

"""
Enter room type (e.g. STANDARD, DELUXE, SUITE):   DELUXE
'  DELUXE' is valid! 
Enter data in (format: room_num, price, type): 101, 2300.86, DELUXE

Successfully instantiated Room object via @classmethod:
Room(101, 2300.86, DELUXE)

"""
