# 🧰 3. zip()
# ✅ What it does:
# zip() pairs items from multiple iterables (like lists or tuples) together.

# 🧪 Examples:

# Example 1: Zipping two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# Output: Alice scored 85, Bob scored 90, Charlie scored 95


# Example 2: Zipping three lists
ages = [25, 30, 35]
for name, score, age in zip(names, scores, ages):
    print(f"{name} is {age} years old and scored {score}")
# Output: Alice is 25 years old and scored 85 ...


# Example 3: Uneven lengths
shorter = [1, 2]
longer = ['a', 'b', 'c']

for x, y in zip(shorter, longer):
    print(x, y)
# Output: (1, 'a'), (2, 'b')  — Stops at the shortest list