"""
Python Sets - Complete Guide with Examples

A set is an unordered, unindexed collection of unique elements.
Mutable, but elements must be hashable (no lists or dicts).
"""

# ----------------------------
# Set Creation
# ----------------------------
print("=== Set Creation ===")

set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])
empty_set = set()  # not {} — that's an empty dict

print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"empty_set = {empty_set}")

# ----------------------------
# Basic Operations
# ----------------------------
print("\n=== Basic Set Operations ===")

set1.add(5)                 # Add a single element
set1.update([6, 7, 8])      # Add multiple elements
set1.discard(2)             # Remove if exists, no error
# set1.remove(99)           # Would raise KeyError if not present

print(f"Updated set1: {set1}")
print(f"Length: {len(set1)}")
print(f"Is 3 in set1? {'Yes' if 3 in set1 else 'No'}")

# ----------------------------
# Set Theory Operations
# ----------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\n=== Set Theory Operations ===")

# Union: All unique elements from both sets
print(f"A | B (Union): {A | B}")
print(f"A.union(B): {A.union(B)}")

# Intersection: Elements common to both sets
print(f"A & B (Intersection): {A & B}")
print(f"A.intersection(B): {A.intersection(B)}")

# Difference: Elements in A but not in B
print(f"A - B (Difference): {A - B}")
print(f"A.difference(B): {A.difference(B)}")

# Symmetric Difference: Elements in A or B but not both
print(f"A ^ B (Symmetric Diff): {A ^ B}")
print(f"A.symmetric_difference(B): {A.symmetric_difference(B)}")

# ----------------------------
# Set Relationships
# ----------------------------
print("\n=== Set Relationships ===")

X = {1, 2}
Y = {1, 2, 3, 4}

print(f"X ⊆ Y (X is subset of Y)? {X.issubset(Y)}")
print(f"Y ⊇ X (Y is superset of X)? {Y.issuperset(X)}")

print(f"Are A and B disjoint? {A.isdisjoint(B)}")  # False, 3 & 4 common

# ----------------------------
# Set Copying and Clearing
# ----------------------------
print("\n=== Copying and Clearing ===")

C = A.copy()
print(f"Copy of A: {C}")

C.clear()
print(f"C after clear(): {C}")

# ----------------------------
# Set Comprehension
# ----------------------------
print("\n=== Set Comprehension ===")

squares = {x**2 for x in range(1, 6)}
print(f"Squares from 1 to 5: {squares}")

# ----------------------------
# Immutable Sets (frozenset)
# ----------------------------
print("\n=== Immutable Sets (frozenset) ===")

fs = frozenset([1, 2, 3, 4])
print(f"frozenset: {fs}")

# fs.add(5) → This would raise an AttributeError, since frozensets are immutable

# ----------------------------
# Summary of Set Operators
# ----------------------------
print("\n=== Summary ===")

print("""
Operator     Method                      Description
--------     ------------------------    -------------------------------
A | B        A.union(B)                  Union
A & B        A.intersection(B)           Intersection
A - B        A.difference(B)             Difference
A ^ B        A.symmetric_difference(B)   Symmetric Difference
A <= B       A.issubset(B)               Subset
A >= B       A.issuperset(B)             Superset
A.isdisjoint(B)                          No common elements
""")
