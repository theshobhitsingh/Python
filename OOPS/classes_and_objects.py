# Define the class 'Car' using the __init__ method to initialize object attributes
class Car:
    # The __init__ method is the constructor of the class
    def __init__(self, brand, model):
        """
        The constructor method initializes a new Car object with brand and model attributes.
        """
        # Instance-level attributes are set using the parameters passed to __init__
        self.brand = brand  # Sets the 'brand' attribute for the object
        self.model = model  # Sets the 'model' attribute for the object

    # Method to display the car's information
    def display_info(self):
        """
        This method returns a string with the car's brand and model.
        """
        return f"This car is a {self.brand} {self.model}."


# Create an instance (object) of the Car class by passing specific attributes to the constructor
my_car = Car("Mercedes", "Benz")

# Print car details directly
print(f"Direct Access - Car brand: {my_car.brand}, Car model: {my_car.model}")

# Create an instance with an empty model
my_car2 = Car("Mercedes", "")  # Passing an empty model value

# Now, 'my_car2' is an object with the brand 'Mercedes' and an empty model
# Direct access print
print(
    f"Direct Access - Car brand: {my_car2.brand}, Car model: {my_car2.model}")

# Calls the method to display info about 'my_car2'
print(my_car2.display_info())  # Output: This car is a Mercedes

# ==========================
# Now using the class with default values for brand and model


class CarWithDefaults:
    def __init__(self, brand="Unknown", model="Unknown"):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"This car is a {self.brand} {self.model}."


# Creating an object without passing any values (uses default values)
default_car = CarWithDefaults()

# Creating an object with passed values
custom_car = CarWithDefaults("Audi", "A6")

# Print the car details using display_info for the default car
print(f"\nUsing display_info method:")
print(default_car.display_info())  # Output: This car is a Unknown Unknown.

# Print the car details using display_info for the custom car
print(custom_car.display_info())   # Output: This car is a Audi A6.