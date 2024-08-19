'''
Objective: 
The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. 

This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

- Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.
'''

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, other_vehicle):
        self.owner = other_vehicle
        return self.owner

car1 = Vehicle('123456', '1967 Ford Mustang', 'Melanie')
car2 = Vehicle('098765', '2015 Buick Encore', 'James')
car3 = Vehicle('444444', '1922 Ford Model T', 'Agnes')

print("\nWhen we started:\n")
print(f"{car1.owner} owned the {car1.type}")
print(f"{car2.owner} owned the {car2.type}")
print(f"{car3.owner} owned the {car3.type}")

car1.update_owner(car2.owner)
car2.update_owner("Steve")
car3.update_owner("DECEASED")

print("\nNow:\n")
print(f"{car1.owner} owns the {car1.type}")
print(f"{car2.owner} owns the {car2.type}")
print(f"{car3.owner} owns the {car3.type}")
