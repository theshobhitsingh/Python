# Multiple Inheritance in Python
# In Python, multiple inheritance allows a class to inherit from more than one parent class. This means that a child class can inherit attributes and methods from multiple base classes. This is useful when a class should be able to take on behaviors from multiple classes without having to combine everything into a single superclass.

# Syntax:
# class ChildClass(ParentClass1, ParentClass2):
#     # Child class implementation
# Key Points about Multiple Inheritance:
# Multiple Inheritance allows the child class to inherit attributes and methods from more than one parent class.

# Method Resolution Order (MRO) determines the order in which classes are searched when a method is called. Python uses a method resolution order algorithm called C3 Linearization to handle this.

# Example Demonstrating Multiple Inheritance:

# Parent Class 1: Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle_info(self):
        return f"This is a {self.brand} {self.model} vehicle."


# Parent Class 2: Electric
class Electric:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def display_battery_info(self):
        return f"This electric vehicle has a {self.battery_size} kWh battery."


# Child Class: ElectricCar, inheriting from both Vehicle and Electric
class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, model, battery_size):
        Vehicle.__init__(self, brand, model)  # Initialize Vehicle class
        Electric.__init__(self, battery_size)  # Initialize Electric class

    # Overriding the display method to combine information from both parent classes
    def display_info(self):
        vehicle_info = self.display_vehicle_info()
        battery_info = self.display_battery_info()
        return f"{vehicle_info} {battery_info}"


# Create an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model 3", 75)

# Display the information from both parent classes using the child class
print(my_electric_car.display_info())
# Explanation of the Example:
# Multiple Inheritance:

# The ElectricCar class inherits from both Vehicle and Electric.

# It combines the attributes and methods from both parent classes. The ElectricCar has access to methods like display_vehicle_info() from Vehicle and display_battery_info() from Electric.

# __init__ Method:

# In the child class ElectricCar, the __init__() method calls the __init__() methods of both parent classes using Vehicle.__init__(self, brand, model) and Electric.__init__(self, battery_size).

# This allows the child class to initialize both the vehicle-related and electric-related attributes.

# Combining Functionality:

# The display_info() method in ElectricCar combines the functionalities of both Vehicle and Electric classes to display full information about the electric car.

# Method Resolution Order (MRO):

# In case of method conflicts or inheritance issues, Python will follow the Method Resolution Order (MRO) to determine the order in which classes are searched for methods and attributes. In this case, Vehicle is searched first, then Electric.

# Output:

# This is a Tesla Model 3 vehicle. This electric vehicle has a 75 kWh battery.
# Advantages of Multiple Inheritance:
# Code Reusability: You can reuse code from multiple parent classes without duplicating logic.

# Flexibility: You can combine behaviors from multiple classes, making the child class more flexible.

# Modularity: Separate classes can handle different functionalities (e.g., Vehicle handles general vehicle details, Electric handles electric-specific details), allowing the system to be more modular.

# Disadvantages of Multiple Inheritance:
# Ambiguity: If two parent classes have methods with the same name, Python has to resolve which one to use. This can lead to ambiguity and unexpected results.

# Complexity: Managing multiple inheritance chains can lead to more complicated code, making it harder to understand and maintain.

# Method Resolution Order (MRO):
# To understand how Python resolves method calls in the case of multiple inheritance, we can check the MRO using the mro() method:

# print(ElectricCar.mro())  # Output the Method Resolution Order
# MRO Output:

# [<class '__main__.ElectricCar'>, <class '__main__.Vehicle'>, <class '__main__.Electric'>, <class 'object'>]
# This shows the order in which Python searches for methods: first in ElectricCar, then in Vehicle, followed by Electric, and finally in object, which is the base class of all classes in Python.

# Key Takeaways:
# Multiple Inheritance allows a child class to inherit from more than one parent class, enabling it to access attributes and methods from multiple sources.

# isinstance() can be used to check if an object is an instance of a class or any of its subclasses, even if those classes are part of a multiple inheritance hierarchy.

# MRO (Method Resolution Order) defines the order in which methods are inherited and resolved in the case of multiple inheritance, helping Python decide which class method to call if there is ambiguity.

# In this example, ElectricCar demonstrates multiple inheritance by inheriting from both the Vehicle and Electric classes, combining their functionalities into one class.
