# ----------------------------------------
# Python Tuples - Comprehensive Overview
# ----------------------------------------

# ✅ What is a Tuple?
# Tuples are immutable sequences in Python used to store multiple items in a single variable.
# Unlike lists, tuples cannot be changed (no add, remove, or update).

# Creating a tuple
empty_tuple = ()  # An empty tuple
single_item_tuple = (5,)  # Single-element tuple (note the comma!)
numbers = (1, 2, 3, 4, 5)  # A tuple of integers
mixed = ("apple", 3.14, 42, True)  # Mixed data types

print("Empty tuple:", empty_tuple)
print("Single item tuple:", single_item_tuple)
print("Numbers:", numbers)
print("Mixed types:", mixed)

# Accessing elements
print("First element:", numbers[0])  # Indexing
print("Last element:", numbers[-1])  # Negative indexing
print("Slice from 1 to 3:", numbers[1:4])  # Slicing

# Tuples are immutable
try:
    numbers[0] = 100  # Will raise TypeError
except TypeError as e:
    print("Error:", e)

# Tuple unpacking
x, y, z = (10, 20, 30)
print("Unpacked x:", x)
print("Unpacked y:", y)
print("Unpacked z:", z)

# Extended unpacking
a, *b, c = (1, 2, 3, 4, 5)
print("a:", a)      # 1
print("b:", b)      # [2, 3, 4]
print("c:", c)      # 5

# Nesting tuples
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Access inner element:", nested[1][0])  # Accessing element 3

# Tuple methods
t = (1, 2, 2, 3, 4, 2)
print("Count of 2:", t.count(2))     # How many times 2 appears
print("Index of 3:", t.index(3))     # First index of 3

# Tuple vs List
# Lists are mutable, tuples are not. Use tuples when data should not change.

# Use case: Returning multiple values from a function
def get_coordinates():
    return (10.5, 22.3)

lat, lon = get_coordinates()
print("Latitude:", lat)
print("Longitude:", lon)

# Tuple as a dictionary key (immutable types only)
my_dict = { (1, 2): "point A", (3, 4): "point B" }
print("Access dict with tuple key:", my_dict[(1, 2)])

# Memory and performance
import sys
list_obj = [1, 2, 3]
tuple_obj = (1, 2, 3)
print("List size:", sys.getsizeof(list_obj))    # More memory
print("Tuple size:", sys.getsizeof(tuple_obj))  # Less memory

# In-built functions that work with tuples
print("Length of tuple:", len(numbers))
print("Max in tuple:", max(numbers))
print("Min in tuple:", min(numbers))
print("Sum of tuple:", sum(numbers))

# Converting between tuples and lists
list_from_tuple = list(numbers)
tuple_from_list = tuple(list_from_tuple)
print("List from tuple:", list_from_tuple)
print("Tuple from list:", tuple_from_list)
