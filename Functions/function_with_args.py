# Define the function to sum all arguments
def sum_of_all(*args):
    """
    This function accepts a variable number of arguments and returns their sum.

    Parameters:
    *args: A variable number of arguments (int, float, etc.).
        - The *args syntax allows us to pass a variable number of arguments to the function.
        - Each argument passed will be treated as an element of a tuple.

    Returns:
    float: The sum of all arguments provided.
        - This function returns the total sum of the numbers passed to it.
    """

    # Print the arguments received to show what was passed to the function
    print("Arguments received:", args)

    # Loop through each argument to perform an operation (e.g., print each argument multiplied by 2)
    for i in args:
        # Print each argument doubled to give an example of how to manipulate each item
        print(i * 2)

    # Sum up all the arguments using the built-in `sum()` function and return the result
    return sum(args)

# Calling the function with different numbers of arguments and printing the result


# 1. Calling sum_of_all with two arguments: 1 and 2
print("Sum:", sum_of_all(1, 2))
# Output: 3 (1 + 2)

# 2. Calling sum_of_all with five arguments: 1, 2, 3, 5, and 7
print("Sum:", sum_of_all(1, 2, 3, 5, 7))
# Output: 18 (1 + 2 + 3 + 5 + 7)

# 3. Calling sum_of_all with four arguments: 1, 2, 2.3, and 466
print("Sum:", sum_of_all(1, 2, 2.3, 466))
# Output: 471.3 (1 + 2 + 2.3 + 466)
