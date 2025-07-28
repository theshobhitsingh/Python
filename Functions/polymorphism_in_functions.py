def multiply(parameter1, parameter2):
    return parameter1 * parameter2


# Test cases
print(multiply(1, 2))           # Output: 2 (1 * 2)
print(multiply("Hello ", 101))  # Output: Hello Hello ... (repeated 101 times)
# Output: OKOKOKOKOKOKOKOKOKOKOKOK... (repeated 100 times)
print(multiply(100, "OK"))
