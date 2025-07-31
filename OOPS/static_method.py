# Define the Car class
class Car:
    # Class variable to keep track of the number of cars created
    car_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1

    def display_info(self):
        return f"This car is a {self.brand} {self.model}."

    # Static method to provide a general description of what a car is
    @staticmethod
    def general_description():
        return "A car is a motor vehicle with wheels, used for transporting passengers."


# Creating instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

# Accessing the static method through the class and an instance
print(Car.general_description())  # Accessing via the class
print(car1.general_description())  # Accessing via an instance

# Displaying information about the cars
print(car1.display_info())  # Output: This car is a Toyota Corolla.
print(car2.display_info())  # Output: This car is a Ford Mustang.
