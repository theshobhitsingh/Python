# Define the Car class
class Car:
    # Class variable to keep track of the number of cars created
    car_count = 0  # Initial car count is set to 0

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model

        # Increment the class variable 'car_count' each time a new Car object is created
        Car.car_count += 1

    def display_info(self):
        return f"This car is a {self.brand} {self.model}."


# Create several instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")
car3 = Car("Tesla", "Model S")

# Print the current car count (should reflect how many cars have been created)
print(f"Total number of cars created: {Car.car_count}")  # Output: 3

# Display information about the cars
print(car1.display_info())  # Output: This car is a Toyota Corolla.
print(car2.display_info())  # Output: This car is a Ford Mustang.
print(car3.display_info())  # Output: This car is a Tesla Model S.
