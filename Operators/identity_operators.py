"""
Identity Operators in Python
Used to compare memory locations of two objects.
"""

x = [1, 2]
y = [1, 2]
z = x  # z points to the same object as x

print("Identity Operators")
print(f"x is z      → {x is z}")     # True → x and z refer to the same object
# False → x and y have same content but different objects
print(f"x is y      → {x is y}")
print(f"x == y      → {x == y}")     # True → values are equal
print(f"x is not y  → {x is not y}")  # True → different objects in memory