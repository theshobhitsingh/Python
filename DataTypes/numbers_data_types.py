"""
Python Number Data Types - Full Guide with Examples

Python has three main numeric types:
1. int      → Integer numbers (whole numbers)
2. float    → Floating-point numbers (decimals)
3. complex  → Complex numbers (real + imaginary)
"""

# ----------------------------
# 1. Integers (int)
# ----------------------------
print("=== Integer (int) ===")

a = 10
b = -300
c = 0

print(f"a = {a}, type: {type(a)}")
print(f"b = {b}, type: {type(b)}")
print(f"c = {c}, type: {type(c)}")

# Python supports arbitrarily large integers
big = 10**100
print(f"Big integer (10^100): {big}, type: {type(big)}\n")

# ----------------------------
# 2. Floating-Point Numbers (float)
# ----------------------------
print("=== Float ===")

x = 10.5
y = -3.14
z = 0.0
scientific = 1.5e2  # 1.5 × 10^2 = 150.0

print(f"x = {x}, type: {type(x)}")
print(f"y = {y}, type: {type(y)}")
print(f"z = {z}, type: {type(z)}")
print(f"Scientific notation (1.5e2): {scientific}, type: {type(scientific)}")

# Floats can behave weirdly due to binary approximation
result = 0.1 + 0.2
# Not exactly 0.3 due to precision limitations
print(f"0.1 + 0.2 = {result}\n")

# ----------------------------
# 3. Complex Numbers (complex)
# ----------------------------
print("=== Complex Numbers ===")

c1 = 3 + 4j
c2 = complex(2, -5)

print(f"c1 = {c1}, type: {type(c1)}")
print(f"c2 = {c2}, type: {type(c2)}")

print(f"Real part of c1: {c1.real}")
print(f"Imaginary part of c1: {c1.imag}")

# Complex arithmetic
sum_ = c1 + c2
product = c1 * c2

print(f"Sum: {sum_}")
print(f"Product: {product}\n")

# ----------------------------
# Type Conversion
# ----------------------------
print("=== Type Conversion ===")

a = 5
b = float(a)
c = int(b)
d = complex(a)

print(f"int to float: {b} ({type(b)})")
print(f"float to int: {c} ({type(c)})")     # Truncates decimals
print(f"int to complex: {d} ({type(d)})")

# Invalid conversion
try:
    bad = int("3.5")  # Raises ValueError
except ValueError as e:
    print(f"Error converting '3.5' to int: {e}\n")

# ----------------------------
# Bonus: Checking with isinstance()
# ----------------------------
print("=== Type Checking with isinstance() ===")

val = 42.0
print(f"isinstance(val, int): {isinstance(val, int)}")     # False
print(f"isinstance(val, float): {isinstance(val, float)}")  # True
# True
print(f"isinstance(val, (int, float)): {isinstance(val, (int, float))}")