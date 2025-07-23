# list_comprehensions.py

# --- 1. Basic List Comprehension ---
print("1. Basic List Comprehension:")
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# --- 2. List Comprehension with Condition (Filtering) ---
print("\n2. List Comprehension with Condition (Filtering):")
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# --- 3. List of Strings with Length Greater Than 3 ---
print("\n3. List of Strings with Length Greater Than 3:")
words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # Output: ['apple', 'banana', 'elephant']

# --- 4. Applying a Function to Each Element ---
print("\n4. Applying a Function to Each Element:")
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# --- 5. Nested List Comprehension ---
print("\n5. Nested List Comprehension (Flattening a 2D list):")
nested_list = [[1, 2, 3], [4, 5], [6, 7]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7]

# --- 6. Creating a List of Tuples ---
print("\n6. Creating a List of Tuples:")
pairs = [(x, x**2) for x in range(5)]
print(pairs)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# --- 7. Using Multiple Conditions ---
print("\n7. Using Multiple Conditions:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_and_divisible_by_3 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(even_and_divisible_by_3)  # Output: [6]

# --- 8. Conditional Logic in the Expression ---
print("\n8. Conditional Logic in the Expression:")
numbers = [1, 2, 3, 4, 5, 6]
result = [x**2 if x % 2 == 0 else x*10 for x in numbers]
print(result)  # Output: [10, 4, 30, 16, 50, 36]

# --- 9. Flattening a Matrix (List of Lists) ---
print("\n9. Flattening a Matrix (List of Lists):")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened_matrix = [element for row in matrix for element in row]
print(flattened_matrix)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Conclusion ---
print("\nEnd of List Comprehensions Examples.")
