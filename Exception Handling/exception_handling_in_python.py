"""
===========================================
        Exception Handling in Python
===========================================

Python provides robust error handling capabilities through its exception
handling system. This file explains all major concepts with examples.

Table of Contents:
1. What are Exceptions?
2. Basic try-except
3. Catching Specific Exceptions
4. Using else with try-except
5. Using finally
6. Catching Multiple Exceptions
7. Custom Exceptions
8. Raising Exceptions
9. Best Practices
"""

# -------------------------------------------------
# 1. What are Exceptions?
# -------------------------------------------------
# An exception is an error that occurs during execution. If not handled,
# it will stop the program.

# Example: ZeroDivisionError
# Uncomment to see it crash the script
# result = 5 / 0

# -------------------------------------------------
# 2. Basic try-except
# -------------------------------------------------
print("\n== Basic try-except ==")
try:
    result = 10 / 0
except:
    print("Something went wrong!")

# -------------------------------------------------
# 3. Catching Specific Exceptions
# -------------------------------------------------
print("\n== Catching specific exception ==")
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Caught an IndexError:", e)

# -------------------------------------------------
# 4. Using else with try-except
# -------------------------------------------------
print("\n== Using else with try-except ==")
try:
    num = int("100")
except ValueError:
    print("Invalid input!")
else:
    print("Conversion successful:", num)

# -------------------------------------------------
# 5. Using finally
# -------------------------------------------------
print("\n== Using finally block ==")
try:
    f = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
    f.close()
finally:
    print("This runs no matter what.")

# -------------------------------------------------
# 6. Catching Multiple Exceptions
# -------------------------------------------------
print("\n== Catching multiple exceptions ==")
try:
    x = int("hello")
    y = 5 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Caught an error:", e)

# -------------------------------------------------
# 7. Custom Exceptions
# -------------------------------------------------
print("\n== Defining and raising custom exceptions ==")


class NegativeNumberError(Exception):
    """Raised when a number is negative."""
    pass


def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return number


try:
    check_positive(-10)
except NegativeNumberError as e:
    print("Custom Error Caught:", e)

# -------------------------------------------------
# 8. Raising Exceptions Manually
# -------------------------------------------------
print("\n== Manually raising exceptions ==")
try:
    raise ValueError("This is a manually raised ValueError")
except ValueError as e:
    print("Caught manually raised error:", e)

# -------------------------------------------------
# 9. Best Practices
# -------------------------------------------------
"""
- Catch specific exceptions instead of using a bare 'except'.
- Avoid catching Exception or BaseException unless necessary.
- Use 'finally' to release external resources like files or DB connections.
- Write meaningful messages in custom exceptions.
- Don't suppress exceptions silently.

Useful built-in exceptions:
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError
- ZeroDivisionError
- AttributeError
"""

# End of file
print("\n✅ Exception Handling Guide Completed.")
