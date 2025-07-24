"""
Bitwise Operators in Python
Operate on bits of integers.
"""

a = 10  # Binary: 1010
b = 4   # Binary: 0100

print("Bitwise Operators")
print(f"a & b  = {a & b}")    # AND → 0000 0100 = 4
print(f"a | b  = {a | b}")    # OR  → 0000 1110 = 14
print(f"a ^ b  = {a ^ b}")    # XOR → 0000 1110 = 14
print(f"~a     = {~a}")       # NOT → -(a + 1) = -11
print(f"a << 1 = {a << 1}")   # Left shift: 1010 << 1 = 10100 = 20
print(f"a >> 1 = {a >> 1}")   # Right shift: 1010 >> 1 = 0101 = 5