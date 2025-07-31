# Define the Car class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model  # Use an underscore to indicate that 'model' is "protected"

    # Property decorator to make 'model' read-only
    @property
    def model(self):
        """
        Getter method for the 'model' attribute. Since we don't define a setter,
        this makes 'model' read-only, meaning it cannot be modified after object creation.
        """
        return self._model  # Return the protected '_model' attribute

    # No setter method defined, making 'model' a read-only property

    # Display method to show car information
    def display_info(self):
        """
        This method returns the information about the car, combining its brand and model.
        """
        return f"This car is a {self.brand} {self.model}."


# Creating an instance of the Car class
my_car = Car("Tesla", "Model S")

# Accessing the model attribute through the property
print(my_car.display_info())  # Output: This car is a Tesla Model S.

# Attempting to modify the model attribute (will raise an error)
try:
    my_car.model = "Model X"  # This will raise an AttributeError since 'model' is read-only
except AttributeError as e:
    print(e)  # Output: can't set attribute

# =======================================================
# **Property Decorators in Python:**

# """
# The `@property` decorator in Python is used to define methods that behave like attributes.
# This allows you to control how an attribute is accessed while still maintaining the ability
# to provide custom logic.

# A Property Decorator achieves:
# 1. **Encapsulation**: By defining a getter method using `@property`, you can control how an attribute is accessed and modified. You can allow read-only access or apply specific logic when accessing the attribute.
# 2. **Getter Method**: The `@property` decorator is used to define the getter method for an attribute. This method is called when accessing the attribute, but it appears like you're accessing a regular attribute.
# 3. **Read-Only Attributes**: If no setter is defined after using `@property`, the attribute becomes read-only. This means you can access it, but cannot modify it after the object is created.
# 4. **Custom Logic**: With `@property`, you can add custom logic (e.g., validation) when accessing the attribute or setting the value, even though the attribute behaves like a regular instance variable.

# ### Example Usage:
# - **Creating a Read-Only Property**: When you only want to allow reading the value of an attribute, you can define a getter method using `@property` but omit the setter.

#   ```python
#   class MyClass:
#       def __init__(self, value):
#           self._value = value

#       @property
#       def value(self):
#           return self._value  # Read-only attribute

#   obj = MyClass(100)
#   print(obj.value)  # This is valid
#   obj.value = 200   # This will raise an error: AttributeError: can't set attribute


# Creating a Property with Getter and Setter: You can define both getter and setter methods for an attribute, which allows you to customize how the attribute is accessed and modified.

# python
# Copy
# Edit
# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value  # Getter method

#     @value.setter
#     def value(self, new_value):
#         if new_value < 0:
#             raise ValueError("Value cannot be negative")
#         self._value = new_value  # Setter method

# obj = MyClass(100)
# print(obj.value)  # Output: 100
# obj.value = 200   # This will update the value
# print(obj.value)  # Output: 200
# obj.value = -1    # This will raise a ValueError
# Key Points:
# Read-Only Property: By using @property without a setter, you make the property read-only. You can access it like a normal attribute but cannot modify it.

# Getter and Setter: The @property decorator allows you to define the getter method, and the @<property_name>.setter decorator allows you to define a setter method.

# Encapsulation: Properties help to enforce data integrity and add logic for getting or setting an attribute, all while keeping the syntax clean and intuitive.

# Benefits:
# Data Integrity: You can prevent invalid data from being set, perform validation, or compute derived values.

# Cleaner Syntax: Properties allow you to use dot notation (i.e., obj.attribute) instead of calling methods (i.e., obj.get_attribute()).

# Flexibility: You can easily modify how an attribute is accessed or set without changing how it's used in other parts of the code.

# In summary, property decorators provide a powerful way to control access to instance attributes, making them an essential tool in object-oriented programming with Python.
# """

# vbnet
# Copy
# Edit

# ### **Explanation of Key Concepts in Comments**:
# - **`@property` Decorator**:
#   - Used to define a **getter method** that behaves like an attribute. It's useful for controlling how the attribute is accessed, validated, or computed.

# - **Read-Only Property**:
#   - When you define a property using `@property` but **do not define a setter method**, the attribute becomes **read-only**, meaning you can access it but cannot modify it.

# - **Getter and Setter**:
#   - A getter method is defined with `@property`, and a setter method is defined using `@<property_name>.setter`. This allows you to control how the value of the property is set, for example, by validating it.

# - **Encapsulation**:
#   - The property allows you to encapsulate the data, meaning you can hide the implementation details (like the internal storage of the data) and provide a clean interface to the user of the class.

# This explanation at the bottom provides an overview of how **property decorators** work in Python, their be
