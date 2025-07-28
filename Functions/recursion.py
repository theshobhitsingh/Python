# Recursive Function to Calculate Factorial of a Number
def factorial(num):
    """
    This function calculates the factorial of a given number using recursion.

    Parameters:
    num (int): The number whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    # Base case: factorial of 0 or 1 is 1
    if num == 0 or num == 1:
        return 1

    # Recursive case: num * factorial of (num - 1)
    return num * factorial(num - 1)


# Ask the user to input a number
try:
    user_input = int(
        input("Please enter a number to calculate its factorial: "))

    if user_input < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate the factorial of the number
        result = factorial(user_input)
        print(f"The factorial of {user_input} is: {result}")

except ValueError:
    print("Invalid input! Please enter an integer.")
