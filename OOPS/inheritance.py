# Parent Class (Super Class)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"This car is a {self.brand} {self.model}."


# Child Class (Sub Class) - Inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size=100):
        # Call the constructor of the parent class using super()
        super().__init__(brand, model)
        self.battery_size = battery_size  # Additional attribute for ElectricCar

    # Override the display_info method to add battery size info
    def display_info(self):
        # Call the parent class method and add new functionality
        return f"{super().display_info()} with a battery size of {self.battery_size} kWh."


# Create an instance of the parent class Car
my_car = Car("Mercedes", "Benz")
print(my_car.display_info())  # This car is a Mercedes Benz.

# Create an instance of the child class ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 85)
# This car is a Tesla Model S with a battery size of 85 kWh.
print(my_electric_car.display_info())
