"""
===========================================
            File Handling in Python
===========================================

Python provides built-in functions to create, read, write, and delete files.
This file demonstrates different operations related to file handling.

Table of Contents:
1. Opening Files
2. Reading Files
3. Writing to Files
4. Appending to Files
5. Using with statement
6. File Modes
7. Working with Binary Files
8. Checking if File Exists
9. Deleting Files
10. Best Practices
"""

import os

# -------------------------------------------------
# 1. Opening Files
# -------------------------------------------------
# The open() function is used to open files.

print("\n== Opening a file ==")
file = open("sample.txt", "w")  # Creates a file if not exists
file.write("Hello, world!\n")
file.close()

# -------------------------------------------------
# 2. Reading Files
# -------------------------------------------------
print("\n== Reading a file ==")
file = open("sample.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()

# -------------------------------------------------
# 3. Writing to Files (overwrite mode)
# -------------------------------------------------
print("\n== Writing to a file (overwrite) ==")
file = open("sample.txt", "w")
file.write("Overwritten content.\n")
file.close()

# -------------------------------------------------
# 4. Appending to Files
# -------------------------------------------------
print("\n== Appending to a file ==")
file = open("sample.txt", "a")
file.write("Appended line.\n")
file.close()

# -------------------------------------------------
# 5. Using 'with' statement (Context Manager)
# -------------------------------------------------
print("\n== Using 'with' to handle files ==")
with open("sample.txt", "r") as file:
    for line in file:
        print("Read line:", line.strip())

# -------------------------------------------------
# 6. File Modes
# -------------------------------------------------
"""
Common modes:
'r'  - Read (default)
'w'  - Write (overwrite)
'a'  - Append
'r+' - Read and Write
'b'  - Binary mode (e.g., 'rb', 'wb')
'x'  - Create and fail if file exists
"""

# -------------------------------------------------
# 7. Working with Binary Files
# -------------------------------------------------
print("\n== Binary file handling ==")
binary_data = bytes([65, 66, 67])
with open("binary_file.bin", "wb") as f:
    f.write(binary_data)

with open("binary_file.bin", "rb") as f:
    data = f.read()
    print("Binary content:", data)

# -------------------------------------------------
# 8. Checking if File Exists
# -------------------------------------------------
print("\n== Checking if a file exists ==")
file_name = "sample.txt"
if os.path.exists(file_name):
    print(f"{file_name} exists.")
else:
    print(f"{file_name} does not exist.")

# -------------------------------------------------
# 9. Deleting Files
# -------------------------------------------------
print("\n== Deleting a file ==")
temp_file = "temp_to_delete.txt"
with open(temp_file, "w") as f:
    f.write("Temporary file.")
if os.path.exists(temp_file):
    os.remove(temp_file)
    print(f"{temp_file} deleted.")
else:
    print("File already deleted.")

# -------------------------------------------------
# 10. Best Practices
# -------------------------------------------------
"""
- Always close files (or use 'with' to do it automatically).
- Handle exceptions with try-except when working with files.
- Avoid hardcoding file paths; use os.path.join().
- For large files, read line by line using a loop.

Example:
with open("large_file.txt", "r") as f:
    for line in f:
        process(line)
"""

# End of file
print("\n✅ File Handling Guide Completed.")
