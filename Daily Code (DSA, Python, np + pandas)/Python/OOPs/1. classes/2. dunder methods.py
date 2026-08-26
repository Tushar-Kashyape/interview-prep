"""
Dunder methods allow custom objects to interact natively with Python's built-in
functions (print(), str(), repr()) and arithmetic/comparison operators (==, +).

__str__: Controls the user-friendly string output when using print() or str().

__repr__: Controls the developer-focused output (unambiguous, helpful for debugging).

__eq__: Overloads the == operator so Python compares object data instead of checking
if two variables point to the exact same memory address.

__add__: Overloads the + operator (e.g., combining the nightly cost of two rooms).



## Why Python has dunder methods, imagine Python asking your custom class:

"I know how to print numbers and add strings, but you just created a Room.
How on earth do I print a Room? How do I add two Room objects together?"

If we don't define __str__ or __repr__, Python falls back to its default behavior,
which prints raw memory addresses.

Python's == operator checks Memory Identity (is), not value equality.

Basically, use default python utilities at object level without any complexities
we have dunder methods over default operators.
"""

class Room:
    def __init__(self, room_number: str, price_per_night: float):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_booked = False

    # Print room for user.
    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return (f"Room {self.room_number} (${self.price_per_night:.2f}/night) -"
                f" {status}")

    # Print details for Dev - logging/ debugging purposes
    def __repr__(self):
        return (f"Room room_number={self.room_number}, "
                f"price_per_night={self.price_per_night}")

    # Custom equality b/w rooms (room1 == romm2)
    def __eq__(self, other) -> bool:
        if not isinstance(other, Room):
            return False

        return self.room_number == other.room_number

    # Operator overloading for '+' (called by room1.price + room2.price)
    def __add__(self, other) -> float:
        if not isinstance(other, Room):
            return NotImplemented

        return self.price_per_night + other.price_per_night

room1_number = input("Enter Room 1 number: ")
price1 = float(input("Enter price for Room 1: "))

room1 = Room(room_number=room1_number, price_per_night=price1)

room2_number = input("Enter Room 2 number: ")
price2 = float(input("Enter price for Room 2: "))

room2 = Room(room_number=room2_number, price_per_night=price2)

print("User view (__str__): ", room1)
print("Dev view (__repr__): ", repr(room1))

if room1 == room2:
    print(f"Room {room1.room_number} and Room {room2.room_number} are duplicate "
          f"room entries")
else:
    print(f"Room {room1.room_number} and Room {room2.room_number} are different "
          f"rooms")

combined_price = room1 + room2
print(f"Combined price per night for {room1.room_number} and {room2.room_number} "
      f"is {combined_price:.2f}")

"""
Enter Room 1 number: 101
Enter price for Room 1: 2300
Enter Room 2 number: 301
Enter price for Room 2: 2500
User view (__str__):  Room 101 ($2300.00/night) - Available
Dev view (__repr__):  Room room_number=101, price_per_night=2300.0
Room 101 and Room 301 are different rooms
Combined price per night for 101 and 301 is 4800.00
"""

