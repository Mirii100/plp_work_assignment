# Polymorphism Demonstration with Animals and Vehicles

class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! 🐟"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! 🦅"

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering! 🐍"

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Vroom vroom! Driving on roads 🚗"

class Boat(Vehicle):
    def move(self):
        return "Splish splash! Sailing on water ⛵"

class Plane(Vehicle):
    def move(self):
        return "Whoosh! Flying through clouds ✈️"

def demonstrate_movement(objects):
    for obj in objects:
        print(obj.move())

# Animal examples
animals = [
    Fish("Nemo"),
    Bird("Eddie"),
    Snake("Monty")
]

# Vehicle examples
vehicles = [
    Car(),
    Boat(),
    Plane()
]

print("=== Animal Movements ===")
demonstrate_movement(animals)

print("\n=== Vehicle Movements ===")
demonstrate_movement(vehicles)