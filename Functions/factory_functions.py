# =============================================================================
# Factory Functions, Bag Theory, and Closures in Python
# =============================================================================
# In Python, functions can be first-class objects, meaning they can be passed around
# and used as arguments just like other objects. This feature opens up various
# programming paradigms such as Factory Functions, Bag Theory, and Closures.
# Let’s break down each concept with detailed comments and examples.

# =============================================================================
# Factory Functions
# =============================================================================
# A **Factory Function** is a function that returns another function.
# These are commonly used in scenarios where you need to generate multiple
# functions with similar logic but different parameters or behavior.
# In other words, the factory function "manufactures" a new function each time.

# -----------------------------------------------------------------------------
# Example of Factory Function
# -----------------------------------------------------------------------------
# Suppose we want to create a function that generates functions for multiplying
# numbers by a given factor. We can use a factory function for this.

def multiplier(factor):
    """
    This function is a factory function. It takes a 'factor' argument and returns
    a new function that multiplies any given number by the provided factor.

    Parameters:
    factor (int or float): The number that other numbers will be multiplied by.

    Returns:
    function: A new function that multiplies numbers by 'factor'.
    """
    def multiply_by_factor(number):
        return number * factor  # Multiplies the given number by the factor
    return multiply_by_factor


# Using the factory function
multiply_by_2 = multiplier(2)  # Creates a function to multiply by 2
multiply_by_3 = multiplier(3)  # Creates a function to multiply by 3

# Test cases
print(multiply_by_2(5))  # Output will be 10 (5 * 2)
print(multiply_by_3(5))  # Output will be 15 (5 * 3)

# -----------------------------------------------------------------------------
# When to Use Factory Functions
# -----------------------------------------------------------------------------
# Factory functions are particularly useful when:
# 1. You need to create multiple functions with similar functionality but different parameters.
# 2. You want to encapsulate a particular behavior and return a customized function for later use.
# 3. You need dynamic creation of functions at runtime.

# =============================================================================
# Bag Theory in Python
# =============================================================================
# **Bag Theory** is a concept derived from functional programming where
# functions can be thought of as "bags" containing multiple elements or arguments.
# These arguments can be used within the function in various ways, including in closures.

# A **bag** refers to a collection of variables, and the **Bag Theory** in Python is often applied
# in cases where we have dynamic collections of values that need to be handled by a function.
# These bags could be lists, tuples, dictionaries, or even other functions.

# -----------------------------------------------------------------------------
# Bag Theory Example: Using `*args` and `**kwargs`
# -----------------------------------------------------------------------------
# Python’s `*args` and `**kwargs` syntax allows us to work with variable
# numbers of arguments, essentially creating a "bag" of parameters.
# This helps us handle functions with an arbitrary number of arguments without
# having to explicitly define each one.


def bag_function(*args, **kwargs):
    """
    This function accepts a variable number of positional and keyword arguments 
    and prints them as a 'bag' of arguments.

    Parameters:
    *args: A tuple containing positional arguments.
    **kwargs: A dictionary containing keyword arguments.
    """
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)


# Test cases
bag_function(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'name': 'Alice', 'age': 25}

# -----------------------------------------------------------------------------
# Benefits of Bag Theory
# -----------------------------------------------------------------------------
# Bag Theory allows:
# 1. Flexibility: You can pass any number of arguments to a function without worrying about the exact number.
# 2. Readability: The syntax of `*args` and `**kwargs` makes it clear that the function can handle many inputs.
# 3. Simplified Code: It avoids the need to explicitly define every possible argument, leading to cleaner code.

# =============================================================================
# Closures in Python
# =============================================================================
# A **Closure** is a function object that remembers values in the enclosing
# scope even after the scope has finished executing. In simpler terms, a closure
# allows a nested function to access variables from its enclosing function.

# -----------------------------------------------------------------------------
# Characteristics of Closures:
# -----------------------------------------------------------------------------
# 1. A closure is created when a function returns another function.
# 2. The inner function remembers the environment in which it was created.
# 3. Closures allow for state retention and can be used to maintain "private" data.

# -----------------------------------------------------------------------------
# Example of Closures
# -----------------------------------------------------------------------------


def outer_function(outer_variable):
    """
    This is the outer function that defines a variable and returns the inner function.

    Parameters:
    outer_variable (int): The variable to be "remembered" by the closure.

    Returns:
    function: An inner function that uses the outer_variable.
    """
    def inner_function(inner_variable):
        """
        This is the inner function that forms the closure.

        Parameters:
        inner_variable (int): A variable passed to the inner function.

        Returns:
        int: The sum of outer_variable and inner_variable.
        """
        return outer_variable + inner_variable  # Uses outer_variable from the outer function
    return inner_function


# Creating a closure
closure_example = outer_function(10)  # outer_variable is 10
result = closure_example(5)  # inner_variable is 5

# Output of the closure function
print(result)  # Output will be 15 (10 + 5)

# -----------------------------------------------------------------------------
# How Closures Work:
# -----------------------------------------------------------------------------
# 1. When `outer_function(10)` is called, it returns `inner_function`.
# 2. The returned `inner_function` has access to the `outer_variable` from `outer_function`.
# 3. Even after `outer_function` finishes executing, the `inner_function` still remembers the `outer_variable`.

# -----------------------------------------------------------------------------
# Closures in Action: Private Variables
# -----------------------------------------------------------------------------
# Closures can be used to create functions with **private state**. This is a powerful feature that allows
# you to encapsulate data and restrict access to it directly.


def counter(start=0):
    """
    This function returns a closure that behaves like a counter.

    Parameters:
    start (int): The starting value of the counter.

    Returns:
    function: A closure that increments the counter each time it is called.
    """
    count = start  # This is the "private" variable

    def increment():
        nonlocal count  # Allows modifying the count variable in the enclosing scope
        count += 1
        return count

    return increment


# Creating a counter closure
my_counter = counter(10)

# Testing the closure
print(my_counter())  # Output will be 11 (10 + 1)
print(my_counter())  # Output will be 12 (11 + 1)
print(my_counter())  # Output will be 13 (12 + 1)

# -----------------------------------------------------------------------------
# Why Closures Are Useful:
# -----------------------------------------------------------------------------
# 1. **Encapsulation**: Closures allow us to encapsulate state and behavior in a single function.
# 2. **Data Privacy**: Closures can help simulate private variables (private to the function).
# 3. **Higher-order Functions**: Closures are useful in creating functions that return other functions, especially in factory functions or callbacks.

# =============================================================================
# Final Code Summary: Factory Functions, Bag Theory, and Closures
# =============================================================================
# Let’s summarize with a simple application of all the concepts discussed above.

# Factory Function Example
double_function = multiplier(2)  # Create a multiplier function
print(double_function(5))  # Output will be 10 (5 * 2)

# Bag Theory Example
bag_function(1, 2, 3, name="John", city="New York")

# Closure Example
closure_result = counter(5)  # Create a counter starting at 5
print(closure_result())  # Output will be 6
print(closure_result())  # Output will be 7

# =============================================================================
# Key Takeaways
# =============================================================================
# 1. **Factory Functions** generate new functions and are useful for dynamic function creation.
# 2. **Bag Theory** allows for flexible handling of multiple arguments using `*args` and `**kwargs`.
# 3. **Closures** allow a function to "remember" its surrounding environment and retain state, providing powerful features like private data and encapsulation.
