# Define a function with a default argument for num2
def fun(num1, num2=54):
    """
    This function takes two numbers and returns their sum. 
    The second number, num2, has a default value of 54.

    Parameters:
    num1 (int or float): The first number to add.
    num2 (int or float, optional): The second number to add. Defaults to 54 if not provided.

    Returns:
    int or float: The sum of num1 and num2.
    """
    # Return the sum of num1 and num2
    return num1 + num2


# Ask the user for their name, providing a default value of "Zen Coder"
name = input("What is your name? (Press Enter to use default: 'Zen Coder') ")

# If the user doesn't provide a name, use "Zen Coder" as the default
if not name:
    name = "Zen Coder"

# Greet the user with the provided or default name
print(f"Hello, {name}! Welcome to the program.")

# Call the function with both arguments (num1 = 1, num2 = 10)
# This will override the default value of num2 and use 10 instead.
# Output will be 1 + 10 = 11
print(f"\nResult when both arguments are provided: {fun(1, 10)}")

# Call the function with only one argument (num1 = 5)
# Since num2 is not provided, it will use the default value of 54 for num2.
# Output will be 5 + 54 = 59
print(f"Result when only one argument is provided: {fun(5)}")
