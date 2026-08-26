"""
Composition means placing one class inside another to build complex systems
("Has-A" relationship).

Instead of writing one massive class that handles everything, we split responsibilities
into separate classes:

A Guest class holds guest information.

A Room class holds room information.

A Booking class holds references to both a Guest instance and a Room instance.
"""

class Guest:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

class Room:

    def __init__(self, room_number: str, price_per_night: float):
        self.room_number = room_number
        # price_per_night: float doesn't confirm expected data type -> typecast
        self.price_per_night = float(price_per_night)

    def __str__(self) -> str:
        return f"Room {self.room_number} ({self.price_per_night:.2f}/night)"

class Booking:

    def __init__(self, guest: Guest, room: Room, nights: int):
        self.guest = guest
        self.room = room
        # price_per_night: float doesn't confirm expected data type -> typecast
        self.nights = int(nights)

    def calculate_cost(self) -> float:
        return self.nights * self.room.price_per_night

    def __str__(self) -> str:
        return (
            f"guest: {self.guest}\n"
            f"room: {self.room}\n"
            f"stay_nights: {self.nights}\n"
            f"Total: {self.calculate_cost():.2f}"
        )


guest_name = input("Enter guest name: ")
guest_email = input("Enter guest email: ")
guest = Guest(name=guest_name, email=guest_email)

room_num = input("\nEnter room number: ")
price = float(input("Enter price per night: "))
room = Room(room_number=room_num, price_per_night=price)

stay_duration = int(input("\nEnter nights to stay: "))

booking_details = Booking(guest=guest, room=room, nights=stay_duration)

print(booking_details)