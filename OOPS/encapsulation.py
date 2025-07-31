class Car:
    def __init__(self, brand, model):
        """
        The constructor method initializes a new Car object with brand and model attributes.
        """
        self.__brand = brand  # Private attribute (Encapsulation)
        self.__model = model  # Private attribute (Encapsulation)

    # Getter method for brand
    def get_brand(self):
        return self.__brand

    # Setter method for brand
    def set_brand(self, brand):
        self.__brand = brand

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        self.__model = model

    # Method to display the car's information
    def display_info(self):
        """
        This method returns a string with the car's brand and model.
        """
        return f"This car is a {self.__brand} {self.__model}."


# Create an instance (object) of the Car class
my_car = Car("Mercedes", "Benz")

# Access and modify brand using getter and setter
print(f"Original brand: {my_car.get_brand()}")  # Output: Mercedes

# Modify the brand using the setter
my_car.set_brand("BMW")

# Print updated brand
print(f"Updated brand: {my_car.get_brand()}")  # Output: BMW

# Directly accessing brand (will cause an error since it's private)
# print(my_car.__brand)  # Uncommenting this will raise an AttributeError

# Using the display_info method
print(my_car.display_info())  # Output: This car is a BMW Benz.


# ==========================
# Now using default values and encapsulation

class CarWithDefaults:
    def __init__(self, brand="Unknown", model="Unknown"):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute

    # Getter method for brand
    def get_brand(self):
        return self.__brand

    # Setter method for brand
    def set_brand(self, brand):
        self.__brand = brand

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        self.__model = model

    # Method to display the car's information
    def display_info(self):
        return f"This car is a {self.__brand} {self.__model}."


# Creating an object with default values
default_car = CarWithDefaults()

# Creating an object with passed values
custom_car = CarWithDefaults("Audi", "A6")

# Print details using display_info method
print(f"\nUsing display_info method:")
print(default_car.display_info())  # Output: This car is a Unknown Unknown.
print(custom_car.display_info())   # Output: This car is a Audi A6.

# Access and modify using getter and setter
default_car.set_brand("Toyota")
default_car.set_model("Corolla")

print(default_car.display_info())  # Output: This car is a Toyota Corolla


# Encapsulation: The practice of bundling the data (attributes) and methods that operate on the data into a single unit (class).
# It helps to hide the internal state of an object and only expose the necessary functionalities to the outside world.

# Access Specifiers in Python:
# 1. **Public Attributes (No underscore or single underscore)**:
#   - These attributes can be accessed and modified directly from outside the class.
#   - Public attributes are generally used when you want the outside world to directly interact with the data.
#   - Example: `self.brand` can be accessed directly from the object.

# 2. **Protected Attributes (Single Leading Underscore `_`)**:
#   - These attributes are still technically public, but by convention, a leading underscore indicates that the attribute is intended for internal use within the class or subclass.
#   - They can be accessed directly, but the underscore suggests they shouldn't be, to avoid misuse.
#   - Example: `self._brand` indicates it should be treated as "protected," but it is still technically accessible.

# 3. **Private Attributes (Double Leading Underscore `__`)**:
#   - These attributes are considered "private" and cannot be accessed directly outside the class.
#   - Python does not enforce strict privacy like some other languages, but it uses a name mangling technique to make it harder to access the attribute directly.
#   - Private attributes are prefixed with `__`, for example, `self.__brand`.
#   - Accessing these attributes directly from outside the class will raise an AttributeError.
#   - This provides better control over how the attribute is used and prevents accidental modifications.

# Getters and Setters:
# - **Getters**: Methods that allow you to retrieve the value of a private attribute.
#   - A getter method provides controlled access to a private attribute.
#   - Example: A getter method for the brand attribute allows the outside world to read the brand but not modify it directly.
#
# - **Setters**: Methods that allow you to modify the value of a private attribute.
#   - A setter method gives you the opportunity to control the modification of the private attribute.
#   - Setters can include validation logic (e.g., ensuring the value is not null, or is of a certain type) before actually changing the value.
#
# **Why use Getters and Setters?**
# - **Control**: They allow you to control how the attribute is accessed and modified, providing a layer of abstraction.
# - **Validation**: You can enforce certain rules or constraints when setting the value (e.g., ensuring a name is not an empty string).
# - **Protection**: You can prevent direct modification of the private attributes, ensuring that only safe values are assigned.
#
# **Example Scenario**:
# - If we have a `Car` class with a `brand` attribute, we might want to control how the brand is set or retrieved.
# - Directly allowing access to `self.__brand` could lead to invalid values being set, so we provide `get_brand()` and `set_brand()` methods instead.
#
# **Advantages of Encapsulation**:
# 1. **Data Protection**: Protects the internal state of an object from being altered in unexpected ways.
# 2. **Modularity**: The internal implementation of a class can be changed without affecting the outside world (users of the class).
# 3. **Flexibility**: Getters and setters allow the internal logic to evolve (e.g., adding validation or logging) without changing how the object is used externally.
# 4. **Debugging**: Errors can be tracked more easily since direct access to attributes is restricted.
