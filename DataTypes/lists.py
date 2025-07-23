# list_operations.py

# --- Creating Lists ---

# Simple list
my_list = [10, 20, 30, 40, 50]
print("Simple list:", my_list)

# List with mixed types
mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with repeated elements
repeated_list = [0] * 5
print("List with repeated elements:", repeated_list)

# --- Accessing Elements ---

print("\nAccessing elements:")
print("Element at index 2:", my_list[2])  # 30
print("Last element using negative index:", my_list[-1])  # 50

# --- Slicing Lists ---

print("\nSlicing lists:")
sublist = my_list[1:4]  # [20, 30, 40]
print("Sliced list from index 1 to 4:", sublist)

step_list = my_list[::2]  # [10, 30, 50]
print("Every other element:", step_list)

# --- Modifying Lists ---

print("\nModifying lists:")

# Changing an element by index
my_list[2] = 99
print("Modified list after changing element at index 2:", my_list)

# Adding elements
my_list.append(60)
print("After appending 60:", my_list)

# Inserting at index 2
my_list.insert(2, 'inserted')
print("After inserting 'inserted' at index 2:", my_list)

# Extending the list with another list
my_list.extend([70, 80])
print("After extending with [70, 80]:", my_list)

# --- Removing Elements ---

print("\nRemoving elements:")

# Remove by value
my_list.remove('inserted')
print("After removing 'inserted':", my_list)

# Remove by index
del my_list[2]
print("After deleting element at index 2:", my_list)

# Pop an element by index and print the popped element
popped_element = my_list.pop(1)
print("Popped element:", popped_element)
print("List after pop:", my_list)

# --- List Methods ---

print("\nList methods:")

# Copy the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Count occurrences of an element
print("Count of 20 in my_list:", my_list.count(20))

# Find index of first occurrence
print("Index of 40 in my_list:", my_list.index(40))

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# Clear the list
my_list.clear()
print("List after clearing:", my_list)

# --- Nested Lists ---

# List of lists (nested list)
nested_list = [[1, 2], [3, 4], [5, 6]]
print("\nNested list:", nested_list)

# Accessing elements in a nested list
print("Accessing nested element [1][1]:", nested_list[1][1])  # 4

# --- List Comprehensions ---

print("\nList comprehensions:")

# Create a list of squares using list comprehension
squares = [x**2 for x in range(5)]
print("Squares of numbers from 0 to 4:", squares)

# Create a list of even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers from 0 to 9:", even_numbers)

# --- Conclusion ---
print("\nEnd of list operations demonstration.")
