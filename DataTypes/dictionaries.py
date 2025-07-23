# dictionaries_with_loops.py

# --- 1. Introduction to Dictionaries ---
print("1. Introduction to Dictionaries:")

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "job": "Engineer"
}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'job': 'Engineer'}

# Accessing values using keys
print("Name:", person["name"])  # Output: Alice
print("Age:", person.get("age"))  # Output: 30

# Using get() with a default value
print("Salary:", person.get("salary", "Not Available"))  # Output: Not Available

# --- 2. Adding and Modifying Elements ---
print("\n2. Adding and Modifying Elements:")

# Adding a new key-value pair
person["salary"] = 70000
print("Updated dictionary with salary:", person)

# Modifying an existing key
person["age"] = 31
print("Updated age:", person)

# --- 3. Removing Elements ---
print("\n3. Removing Elements:")

# Using del to remove a key-value pair
del person["job"]
print("After deleting job:", person)

# Using pop() to remove a key-value pair and get the value
age = person.pop("age")
print("Popped age:", age)  # Output: 31
print("After popping age:", person)

# Using popitem() to remove the last key-value pair
last_item = person.popitem()
print("Popped last item:", last_item)  # Output: ('salary', 70000)
print("After popitem:", person)

# Using clear() to remove all items
person.clear()
print("After clearing the dictionary:", person)  # Output: {}

# --- 4. Dictionary Methods ---
print("\n4. Dictionary Methods:")

# Recreate the original dictionary
person = {
    "name": "Alice",
    "age": 30,
    "job": "Engineer"
}

# Keys and Values
print("Keys:", person.keys())  # Output: dict_keys(['name', 'age', 'job'])
print("Values:", person.values())  # Output: dict_values(['Alice', 30, 'Engineer'])

# Items (key-value pairs)
print("Items:", person.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('job', 'Engineer')])

# Copying a dictionary
person_copy = person.copy()
print("Copied dictionary:", person_copy)

# --- 5. Nested Dictionaries ---
print("\n5. Nested Dictionaries:")

# A dictionary inside a dictionary
employee = {
    "name": "John",
    "age": 40,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zipcode": "10001"
    }
}

# Accessing nested dictionary values
print("Employee name:", employee["name"])  # Output: John
print("Employee city:", employee["address"]["city"])  # Output: New York

# --- 6. Dictionary Comprehension ---
print("\n6. Dictionary Comprehension:")

# Create a dictionary with square values
squares = {x: x**2 for x in range(5)}
print("Dictionary with squares:", squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Create a dictionary of even numbers
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print("Dictionary with even numbers:", even_dict)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# --- 7. Merging Dictionaries ---
print("\n7. Merging Dictionaries:")

# Using the update() method to merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print("After merging dict2 into dict1:", dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using dictionary unpacking (Python 3.5+)
merged_dict = {**dict1, **dict2}
print("Merged dictionary using unpacking:", merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# --- 8. Iterating over a Dictionary ---
print("\n8. Iterating over a Dictionary:")

# Iterating through keys
print("Keys:")
for key in person.keys():
    print(key)

# Iterating through values
print("\nValues:")
for value in person.values():
    print(value)

# Iterating through key-value pairs
print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

# --- 9. Looping to Modify Values ---
print("\n9. Looping to Modify Values:")

# Increase age by 1 if it is less than 40
for key, value in person.items():
    if key == "age" and value < 40:
        person[key] = value + 1
print("After incrementing age:", person)

# Adding a title to each job
jobs = {"Alice": "Engineer", "Bob": "Designer", "Charlie": "Manager"}
for person, job in jobs.items():
    jobs[person] = f"Senior {job}"
print("After adding 'Senior' to jobs:", jobs)

# --- 10. Conditional Deletion in Loop ---
print("\n10. Conditional Deletion in Loop:")

# Remove entries where the value is a string
person = {"name": "Alice", "age": 30, "job": "Engineer"}
keys_to_delete = []
for key, value in person.items():
    if isinstance(value, str):  # Check if the value is a string
        keys_to_delete.append(key)

for key in keys_to_delete:
    del person[key]

print("After removing string values:", person)  # Output: {'age': 30}

# --- 11. Handling Missing Keys (Exception Handling) ---
print("\n11. Handling Missing Keys:")

# Using try-except for missing keys
try:
    print(person["salary"])
except KeyError:
    print("Key 'salary' not found!")

# Using the setdefault() method
person = {"name": "Alice", "age": 30}
salary = person.setdefault("salary", 50000)
print("Salary (using setdefault):", salary)  # Output: 50000
print("Updated dictionary:", person)

# --- 12. Dictionary with Default Values (defaultdict) ---
print("\n12. Dictionary with Default Values (defaultdict):")
from collections import defaultdict

# Using defaultdict to handle missing keys with a default value
dd = defaultdict(int)  # Default value is int() -> 0
dd["a"] = 1
dd["b"] = 2
print("defaultdict:", dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print("Default value for missing key 'c':", dd["c"])  # Output: 0

# --- Conclusion ---
print("\nEnd of Dictionary Operations Demonstration.")
