"""
At its foundation, a class is a blueprint. Creating an object from a class constructs
an instance in memory.

__init__: The constructor method that executes automatically when a new object is
created.

self: The explicit reference to the current instance being accessed or modified.

Instance Attributes: Variables attached to self that belong uniquely to that specific
object.
"""

class Room:

    def __init__(self, room_number: str, price_per_night: float):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_booked = False

    def book_room(self):
        self.is_booked = True

    def calculate_cost(self, nights: int) -> float:
        return self.price_per_night * nights


room_num = input("Enter room number: ")
price = int(input("Enter price per night: "))

room = Room(room_number=room_num, price_per_night=price)

nights = int(input("Enter number of nights for which room to be booked: "))
total_price = room.calculate_cost(nights=nights)

print(f"\n[Booked] Room {room.room_number} at {room.price_per_night}/ night")
print(f"Total price for {nights}: {total_price}")

"""
O/p:

Enter room number: 301
Enter price per night: 2300
Enter number of nights for which room to be booked: 3

[Booked] Room 301 at 2300/ night
Total price for 3: 6900
"""

