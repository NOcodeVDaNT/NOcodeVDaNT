# 1. Encapsulation: Bundling data and methods that work on that data into a single unit (class)

class Car:
    def __init__(self, make, model, year):
        self.make = make  # Instance variable for car make
        self.model = model  # Instance variable for car model
        self.year = year  # Instance variable for car year
        self.__engine_status = "Off"  # Private variable, encapsulated (can't be accessed directly)

    def start_engine(self):
        self.__engine_status = "On"  # Encapsulated method to change the engine status
        print(f"The engine of {self.year} {self.make} {self.model} is {self.__engine_status}.")

    def stop_engine(self):
        self.__engine_status = "Off"  # Encapsulated method to change the engine status
        print(f"The engine of {self.year} {self.make} {self.model} is {self.__engine_status}.")

    def get_engine_status(self):
        return self.__engine_status  # Encapsulated method to access the engine status


# 2. Abstraction: Hiding the complex implementation and showing only the essential features

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        pass  # Abstract method that should be implemented by subclasses


class CarAbstract(Vehicle):
    def start(self):
        print(f"The {self.make} {self.model} is now starting.")
        
    def stop(self):
        print(f"The {self.make} {self.model} is now stopping.")


# 3. Inheritance: A way to form new classes using classes that have already been defined

class ElectricCar(CarAbstract):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)  # Calling the parent class constructor
        self.battery_size = battery_size  # ElectricCar has an additional attribute

    def charge(self):
        print(f"The {self.make} {self.model} is charging with {self.battery_size}-kWh battery.")


# 4. Polymorphism: The ability to use a single method in different ways

class Truck(CarAbstract):
    def start(self):
        print(f"The truck {self.make} {self.model} is now starting with a loud roar!")

    def load_cargo(self):
        print(f"Loading cargo in {self.make} {self.model} truck.")


# Demonstrating the OOP concepts:

# Encapsulation example:
car = Car("Toyota", "Camry", 2022)
car.start_engine()  # The engine status is encapsulated, we can only change it through the method
car.stop_engine()

# Abstraction example:
electric_car = ElectricCar("Tesla", "Model 3", 75)
electric_car.start()  # Starts the electric car (abstract method implementation)
electric_car.charge()

# Inheritance example:
truck = Truck("Ford", "F-150")
truck.start()  # Truck class inherits start method from CarAbstract but overrides it
truck.load_cargo()

# Polymorphism example:
vehicles = [electric_car, truck]

# Using the same method 'start' but with different behaviors for electric car and truck
for vehicle in vehicles:
    vehicle.start()

