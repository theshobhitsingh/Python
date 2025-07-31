# Class Inheritance in Python:
# Inheritance allows a class (the subclass) to inherit attributes and methods from another class (the superclass). This mechanism promotes code reusability and establishes a natural hierarchy between classes. A subclass can extend or modify the functionality of a superclass by overriding methods or adding new methods.

# isinstance() Function:
# The isinstance() function is used to check if an object is an instance of a specific class or a tuple of classes. This function is useful in scenarios where you need to ensure that an object is an instance of a particular class or its subclass.

# Syntax:
# isinstance(object, classinfo)
# object: The object to be checked.

# classinfo: A class or a tuple of classes to check against.

# Example Demonstrating Inheritance and isinstance():

# Parent (Super) Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"This car is a {self.brand} {self.model}."


# Child (Sub) Class inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size=100):
        super().__init__(brand, model)  # Call the constructor of the parent class
        self.battery_size = battery_size  # Additional attribute for ElectricCar

    def display_info(self):
        # Call the parent class's method and add new information
        return f"{super().display_info()} with a battery size of {self.battery_size} kWh."


# Create an instance of ElectricCar
my_electric_car = ElectricCar("Tesla", "Model 3", 75)

# Checking if 'my_electric_car' is an instance of Car
# Output: True (since ElectricCar is a subclass of Car)
print(isinstance(my_electric_car, Car))

# Checking if 'my_electric_car' is an instance of ElectricCar
print(isinstance(my_electric_car, ElectricCar))  # Output: True

# Checking if 'my_electric_car' is an instance of an unrelated class
# Output: False (ElectricCar is not a subclass of str)
print(isinstance(my_electric_car, str))

# Display car info
# Output: This car is a Tesla Model 3 with a battery size of 75 kWh.
print(my_electric_car.display_info())

# Explanation:
# Class Inheritance:

# Car is the parent (super) class.

# ElectricCar is the child (sub) class that inherits from Car.

# ElectricCar inherits the __init__ and display_info methods from Car, but it overrides the display_info method to include battery information.

# super().__init__(brand, model) calls the constructor of the parent class, allowing the child class to initialize the attributes defined in the parent class.

# isinstance() Function:

# The isinstance() function checks if an object is an instance of a specific class or any of its subclasses.

# isinstance(my_electric_car, Car) returns True because ElectricCar is a subclass of Car.

# isinstance(my_electric_car, ElectricCar) also returns True because the object is indeed an instance of the ElectricCar class.

# isinstance(my_electric_car, str) returns False because ElectricCar is not related to str.

# Output:
# True
# True
# False
# This car is a Tesla Model 3 with a battery size of 75 kWh.
# Key Points:
# Inheritance:

# In Python, a class can inherit attributes and methods from another class using class inheritance. This is achieved by specifying the parent class in the parentheses when defining the child class.

# A child class can extend or override methods and attributes from the parent class.

# isinstance():

# isinstance() is used to check if an object is an instance of a specific class or a subclass of it.

# It returns True if the object is an instance of the specified class or any of its subclasses, and False otherwise.

# When to Use isinstance():
# Type Checking: You can use isinstance() when you need to confirm that an object is of a certain class before performing operations on it.

# Polymorphism: In a scenario where multiple classes have a similar interface, you can use isinstance() to determine which class an object belongs to and call appropriate methods.

# In this example, the ElectricCar class inherits from Car, and we use isinstance() to check the type of the object, demonstrating both inheritance and type checking in Python.
