# 🧰 2. enumerate()
# ✅ What it does:
# enumerate() adds a counter (index) to an iterable and returns it as an enumerate object.

# 🧪 Examples:
# Example 1: Getting index and value

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output: Index 0: apple, Index 1: banana, Index 2: cherry


# Example 2: Start index from 1

for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")
# Output: Item 1: apple, Item 2: banana, Item 3: cherry