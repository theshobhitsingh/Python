# Python Functions: Everything You Need to Know

# Function Definition
# A function is defined using the 'def' keyword followed by the function name and parameters.
# Here, we define a simple function 'greet' that takes no parameters.
def greet():
    # This line prints a simple greeting message when the function is called
    print("Hello, welcome to the world of Python!")


# Calling the function 'greet' will execute the code inside the function
greet()


# 1. Function with Parameters
# Parameters are variables that are passed into a function when it is called.
# Let's define a function that takes a name and prints a personalized greeting.

def greet_person(name):
    # The function takes 'name' as an argument and prints a greeting for that person
    print(f"Hello, {name}!")


# Calling the function with an argument 'John'
greet_person("John")


# 2. Return Statement
# A function can also return a value using the 'return' keyword.
# Let's define a function that calculates the square of a number.

def square_of_number(num):
    # The function takes a number and returns its square
    return num ** 2


# Calling the function and storing the result in a variable
result = square_of_number(5)
# Printing the returned value (square of 5)
print(f"The square of 5 is: {result}")


# 3. Function with Multiple Parameters
# A function can have multiple parameters. Let's define a function to add two numbers.

def add_numbers(a, b):
    # The function takes two numbers as arguments and returns their sum
    return a + b


# Calling the function with two numbers
sum_result = add_numbers(3, 4)
# Printing the result (sum of 3 and 4)
print(f"The sum of 3 and 4 is: {sum_result}")


# 4. Lambda Functions
# Lambda functions are small anonymous functions defined with the 'lambda' keyword.
# They can have any number of parameters but only one expression.

# This lambda function takes two parameters and returns their sum
def add(x, y): return x + y


print(f"Lambda sum of 5 and 6 is: {add(5, 6)}")


# 5. Function Scope
# Variables defined inside a function are local to that function and can't be accessed outside.
# Let's see an example:

def local_variable_example():
    # This variable is local to the function
    local_var = 10
    print(f"Local variable inside function: {local_var}")


# Calling the function will print the local variable value
local_variable_example()

# Uncommenting the next line will cause an error because 'local_var' is not accessible outside the function
# print(local_var)  # This will raise a NameError


# 6. Function with Default Parameters
# Python allows us to set default values for parameters. If the argument is not provided, the default value is used.

def greet_with_default(name="Guest"):
    # If 'name' is not passed, it will default to "Guest"
    print(f"Hello, {name}!")


# Calling the function with a custom name
greet_with_default("Alice")
# Calling the function without passing any argument, will use the default value
greet_with_default()


# 7. Recursion
# A function can call itself. This is known as recursion. Recursion must have a base case to avoid infinite loops.
# Let's define a simple recursive function to calculate the factorial of a number.

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n * factorial of (n-1)
    else:
        return n * factorial(n-1)


# Calling the recursive function to find the factorial of 5
print(f"The factorial of 5 is: {factorial(5)}")


# Function Best Practices

# 1. Function names should be descriptive and follow naming conventions (e.g., snake_case).
# 2. Functions should be small and perform a single task (single responsibility principle).
# 3. Use docstrings to document the purpose of the function and its parameters/returns.

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    Arguments:
    a -- The first number
    b -- The second number
    """
    return a * b


# Calling the function and printing the result
print(f"Multiplying 4 and 5 gives: {multiply(4, 5)}")


# Conclusion
# Functions are essential tools in Python for code organization, reusability, and clarity.
# They help you break down complex problems into smaller, easier-to-manage parts.
