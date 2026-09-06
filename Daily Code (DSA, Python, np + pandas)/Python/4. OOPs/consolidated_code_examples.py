from abc import ABC, abstractmethod

# Basic Inheritance + super():

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)                  # parent handles self.name
        self.breed = breed                      # child adds its own attribute

d = Dog("Rex", "Labrador")
print(d.name, d.breed)
print(d.speak())

# ==============================================================================

# Method Overriding: replace vs extend

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"         # overrides Animal.speak entirely

class Dog2(Animal):
    def speak(self):
        base = super().speak()                  # calls PARENT's version too, then
        return f"{base}, specifically a bark"   # extends it.

print(Cat("Whiskers").speak())
print(Dog2("Rex").speak())

# ==============================================================================

# Polymorphism (duck typing, no shared explicit interface needed)

class Duck:
    def speak(self):
        return "Quack"

animals = [Cat("Tom"), Dog2("Rex"), Duck()]
for animal in animals:
    print(animal.speak())

# ==============================================================================

# isinstance() vs type()
print(isinstance(d, Animal))            # True — respects inheritance
print(type(d) == Animal)                # False — Dog is not exactly Animal

# ==============================================================================

# Encapsulation:

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        self.__pin = "1234"

    def get_balance(self):
        return self._balance

acc = BankAccount(1000)
print(acc._balance)                 # works, but conventionally "don't do this"
print(acc.get_balance())            # correct way: via a method
# print(acc.__pin)                  # AttributeError — name mangled
print(acc._BankAccount__pin)        # works — mangling isn't true security, just
                                    # obscurity

# ==============================================================================

# MRO with multiple inheritance:

class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):                  # inherits from BOTH A and B
    pass

c = C()
print(c.greet())                # "Hello from A" — A comes first in C(A, B)
print(C.__mro__)                # shows exact lookup order: C -> A -> B -> object

# ==============================================================================

# Diamond Inheritance - MRO really matters here

class Base:
    def who(self):
        return "Base"

class Left(Base):
    def who(self):
        return "Left"

class Right(Base):
    def who(self):
        return "Right"

class Diamond(Left, Right):
    pass

print(Diamond().who())              # "Left" — follows MRO, not naive depth-first
print(Diamond.__mro__)              # Diamond -> Left -> Right -> Base -> object

# ==============================================================================

# Abstract Base Classes (ABCs):

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

# print(Shape())                    # would raise TypeError — can't instantiate
                                    # abstract class directly
print(Circle(5).area())             # fine — Circle implements the required area()

# If Circle didn't define area(), instantiating it would raise TypeError.
# Python's way of enforcing an interface contract, genuinely used in real codebases.

# ==============================================================================

# Duck typing - Python:

class Duck:
    def quack(self):
        return "Quack, quack"

class Person:
    def quack(self):
        return "I'm pretending to be a duck: Quack!"

def make_it_quack(thing):
    print(thing.quack())

ducky = Duck()
human = Person()

make_it_quack(ducky)
make_it_quack(human)





