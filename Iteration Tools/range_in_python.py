# 🧰 1. range()
# ✅ What it does:
# range() generates a sequence of numbers, commonly used in for loops.

# 🧪 Examples:

# Example 1: Basic loop with range()
# Print numbers from 0 to 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4


# Example 2: Starting from a specific number
# Print numbers from 2 to 6
for i in range(2, 7):
    print(i)
# Output: 2, 3, 4, 5, 6


# Example 3: Using a step
# Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10


# Example 4: Counting backward
# Print numbers in reverse from 5 to 1
for i in range(5, 0, -1):
    print(i)
# Output: 5, 4, 3, 2, 1