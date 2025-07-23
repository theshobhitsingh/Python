# dictionary_comprehensions.py

# --- 1. Basic Dictionary Comprehension ---
print("1. Basic Dictionary Comprehension:")

# Create a dictionary where keys are numbers and values are their squares
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# --- 2. Dictionary Comprehension with Condition ---
print("\n2. Dictionary Comprehension with Condition:")

# Create a dictionary of even numbers, with the values as their squares
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# --- 3. Using an Expression for Values ---
print("\n3. Using an Expression for Values:")

# Create a dictionary where keys are strings and values are the lengths of those strings
words = ["apple", "banana", "kiwi", "grape"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # Output: {'apple': 5, 'banana': 6, 'kiwi': 4, 'grape': 5}

# --- 4. Create a Dictionary from Two Lists ---
print("\n4. Create a Dictionary from Two Lists:")

# Two lists, one for keys and one for values
keys = ["name", "age", "job"]
values = ["Alice", 30, "Engineer"]

# Create a dictionary using the lists
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'job': 'Engineer'}

# --- 5. Dictionary Comprehension with Nested Loops ---
print("\n5. Dictionary Comprehension with Nested Loops:")

# Create a dictionary where the keys are pairs of numbers, and the values are their products
product_dict = {(x, y): x * y for x in range(3) for y in range(3)}
print(product_dict)  # Output: {(0, 0): 0, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 1, (1, 2): 2, (2, 0): 0, (2, 1): 2, (2, 2): 4}

# --- 6. Creating a Dictionary with Conditional Expressions ---
print("\n6. Creating a Dictionary with Conditional Expressions:")

# Dictionary with condition inside the comprehension
numbers = [1, 2, 3, 4, 5, 6]
result = {x: ("Even" if x % 2 == 0 else "Odd") for x in numbers}
print(result)  # Output: {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd', 6: 'Even'}

# --- 7. Reversing a Dictionary ---
print("\n7. Reversing a Dictionary:")

# Create a dictionary with keys as numbers and values as strings
original_dict = {1: "a", 2: "b", 3: "c"}

# Reverse the dictionary (swap keys and values)
reversed_dict = {value: key for key, value in original_dict.items()}
print(reversed_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# --- 8. Filtering Dictionary Items ---
print("\n8. Filtering Dictionary Items:")

# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(10)}

# Filter the dictionary to only include values greater than 20
filtered_squares = {k: v for k, v in squares_dict.items() if v > 20}
print(filtered_squares)  # Output: {5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# --- 9. Using Dictionary Comprehensions with Functions ---
print("\n9. Using Dictionary Comprehensions with Functions:")

# Function to calculate the cube of a number
def cube(x):
    return x ** 3

# Create a dictionary of numbers and their cubes
cubes = {x: cube(x) for x in range(5)}
print(cubes)  # Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# --- 10. Creating a Dictionary with a Default Value (defaultdict) ---
print("\n10. Creating a Dictionary with a Default Value (defaultdict):")
from collections import defaultdict

# Create a defaultdict that returns 0 if a key doesn't exist
dd = defaultdict(int)

# Add some values
dd["apple"] += 1
dd["banana"] += 2
dd["apple"] += 3

print(dd)  # Output: defaultdict(<class 'int'>, {'apple': 4, 'banana': 2})
print(dd["orange"])  # Output: 0 (default value for missing key)

# --- Conclusion ---
print("\nEnd of Dictionary Comprehensions Demonstration.")
