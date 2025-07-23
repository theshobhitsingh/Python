"""
Python Strings - Deep Dive Guide

Strings in Python are:
- Immutable
- Ordered sequences of Unicode characters
- Surrounded by '', "", ''' ''' or """ """

"""

# ----------------------------
# 1. String Creation
# ----------------------------
print("=== String Creation ===")

s1 = 'Hello'
s2 = "World"
s3 = '''Multiline
String'''
s4 = "He said, \"Yes!\""

print(s1, s2)
print(s3)
print(s4)

# ----------------------------
# 2. Indexing and Slicing
# ----------------------------
print("\n=== Indexing and Slicing ===")

text = "Python"

# Indexing (0-based)
print(f"text[0] = {text[0]}")
print(f"text[-1] = {text[-1]}")  # Last character

# Slicing
print(f"text[1:4] = {text[1:4]}")    # yth
print(f"text[:3] = {text[:3]}")      # Pyt
print(f"text[3:] = {text[3:]}")      # hon
print(f"text[::-1] = {text[::-1]}")  # Reverse

# ----------------------------
# 3. Immutability
# ----------------------------
print("\n=== Immutability ===")

try:
    text[0] = 'J'  # This will raise an error
except TypeError as e:
    print(f"Strings are immutable: {e}")

# ----------------------------
# 4. String Concatenation and Repetition
# ----------------------------
print("\n=== Concatenation and Repetition ===")

a = "Hello"
b = "World"

print(a + " " + b)       # Concatenation
print((a + "! ") * 3)    # Repetition

# ----------------------------
# 5. Membership and Length
# ----------------------------
print("\n=== Membership and Length ===")

word = "developer"
print(f"'dev' in word → {'dev' in word}")  # True
print(f"Length of word: {len(word)}")

# ----------------------------
# 6. Useful String Methods
# ----------------------------
print("\n=== Common String Methods ===")

s = "  Hello, Python  "

print(f"Original: '{s}'")
print(f"s.strip(): '{s.strip()}'")           # Remove whitespace
print(f"s.lower(): {s.lower()}")             # lowercase
print(f"s.upper(): {s.upper()}")             # UPPERCASE
print(f"s.replace('Python', 'World'): {s.replace('Python', 'World')}")
print(f"s.find('lo'): {s.find('lo')}")       # Index of substring
print(f"s.startswith('  He'): {s.startswith('  He')}")
print(f"s.endswith('on  '): {s.endswith('on  ')}")

# ----------------------------
# 7. String Splitting and Joining
# ----------------------------
print("\n=== Split and Join ===")

data = "apple,banana,cherry"
fruits = data.split(",")
print(f"Split: {fruits}")

joined = " | ".join(fruits)
print(f"Joined: {joined}")

# ----------------------------
# 8. String Formatting
# ----------------------------
print("\n=== String Formatting ===")

name = "Alice"
age = 30

# Old-style formatting
print("Hello %s, you are %d" % (name, age))

# str.format()
print("Hello {}, you are {}".format(name, age))

# f-strings (Python 3.6+)
print(f"Hello {name}, you are {age}")

# Format numbers
pi = 3.1415926
print(f"Pi rounded: {pi:.2f}")  # 2 decimal places

# ----------------------------
# 9. Character Checks
# ----------------------------
print("\n=== Character Checks ===")

s = "Python123"

print(f"s.isalpha(): {s.isalpha()}")      # False, contains digits
print(f's[:6].isalpha(): {s[:6].isalpha()}')  # True
print(f"s.isdigit(): {s.isdigit()}")      # False
print(f"s.isalnum(): {s.isalnum()}")      # True (letters + numbers)
print(f"'   '.isspace(): {'   '.isspace()}")  # True

# ----------------------------
# 10. Unicode & Encoding
# ----------------------------
print("\n=== Unicode & Encoding ===")

char = '✓'
code_point = ord(char)
back_to_char = chr(code_point)

print(f"Character: {char}, Code Point: {code_point}")
print(f"Back to character: {back_to_char}")

encoded = char.encode('utf-8')
print(f"UTF-8 Encoded: {encoded}")
print(f"Decoded: {encoded.decode('utf-8')}")

# ----------------------------
# 11. Raw Strings and Escape Characters
# ----------------------------
print("\n=== Raw Strings and Escape Sequences ===")

print("Line1\\nLine2 →", "Line1\nLine2")
print(r"Raw string (r'Line1\nLine2') →", r"Line1\nLine2")

# ----------------------------
# 12. Multiline Strings
# ----------------------------
print("\n=== Multiline Strings ===")

multi = """This is a
multiline string
with line breaks"""
print(multi)
