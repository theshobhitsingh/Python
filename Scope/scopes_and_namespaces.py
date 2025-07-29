# =============================================================================
# Scopes and Namespaces in Python
# =============================================================================
# In Python, the concepts of **Scopes** and **Namespaces** are fundamental
# for understanding how the interpreter looks up variables and resolves their values.
# These concepts are crucial when working with variables, functions, and classes,
# especially when dealing with situations where the same variable names might appear in different contexts.

# =============================================================================
# What is a Namespace?
# =============================================================================
# A **namespace** is a container where names (identifiers) are mapped to objects (values).
# A namespace ensures that each name is unique within its scope, thus preventing conflicts between variable names.

# -----------------------------------------------------------------------------
# Types of Namespaces
# -----------------------------------------------------------------------------
# 1. **Built-in Namespace**:
# - This namespace contains all the built-in objects provided by Python (e.g., `print()`, `id()`, `int()`, etc.).
# - It is always available to the Python interpreter.

# 2. **Global Namespace**:
# - This namespace exists for the module or script in which you are running.
# - It includes functions, classes, variables, etc., defined in the main body of the script or module.

# 3. **Enclosing Namespace**:
# - This refers to namespaces that exist in functions that are nested within other functions.
# - For example, in a function inside another function, the outer function’s variables are accessible to the inner function.

# 4. **Local Namespace**:
# - This namespace contains names (variables, functions, etc.) defined within the current function.
# - These are local to the function or block of code.

# =============================================================================
# What is Scope?
# =============================================================================
# The **scope** refers to the region of the program where a namespace is directly accessible.
# It controls the visibility and lifecycle of variables. Python follows a scope resolution mechanism
# called the **LEGB** rule to determine where to look for variables.

# =============================================================================
# LEGB Rule (Local, Enclosing, Global, Built-in)
# =============================================================================
# When Python encounters a variable name, it searches for it in the following order:
#
# 1. **Local (L)**:
#    - The local namespace refers to the innermost scope, i.e., the current function where the variable is being accessed.
# 2. **Enclosing (E)**:
#    - If the variable is not found in the local scope, Python looks for it in any enclosing scopes (e.g., functions that contain other functions).
# 3. **Global (G)**:
#    - If the variable is not found in local or enclosing scopes, Python checks the global namespace (the script or module level).
# 4. **Built-in (B)**:
#    - If Python cannot find the variable in any of the previous scopes, it looks in the built-in namespace (which contains Python’s built-in functions and objects).

# =============================================================================
# Detailed Explanation of LEGB Rule
# =============================================================================
# Let’s break down the LEGB rule further by analyzing each type of scope:

# -----------------------------------------------------------------------------
# 1. Local Scope (L)
# -----------------------------------------------------------------------------
# This is the most immediate scope. Variables defined inside a function are in the local scope.
# These variables are **only accessible inside the function**.

def example_function():
    a = 5  # 'a' is in the local scope
    print(a)  # Prints 5


example_function()

# -----------------------------------------------------------------------------
# 2. Enclosing Scope (E)
# -----------------------------------------------------------------------------
# If you have nested functions, the enclosing scope refers to the scope of the outer function.
# Variables defined in an outer function are accessible to the inner functions, but **not vice versa**.


def outer_function():
    x = 10  # Variable 'x' is in the enclosing scope

    def inner_function():
        print(x)  # Accessing 'x' from the enclosing scope

    inner_function()


outer_function()

# -----------------------------------------------------------------------------
# 3. Global Scope (G)
# -----------------------------------------------------------------------------
# The global scope exists at the module level. Variables defined in the global namespace
# are accessible from anywhere in the file, but **only after the point where they are defined**.

y = 15  # 'y' is in the global scope


def my_function():
    print(y)  # Accessing the global variable 'y'


my_function()

# -----------------------------------------------------------------------------
# 4. Built-in Scope (B)
# -----------------------------------------------------------------------------
# The built-in scope is the widest scope, containing all built-in objects and functions provided by Python.
# This scope is always available and includes things like `print()`, `len()`, `int()`, etc.

print("Hello, World!")  # 'print' is a built-in function

# =============================================================================
# Modifying Global Variables Inside Functions
# =============================================================================
# By default, you cannot modify a global variable inside a function directly unless you use the `global` keyword.

x = 10  # Global scope


def modify_global():
    global x  # Declare that we are using the global 'x'
    x = 20  # Modify the global 'x'


modify_global()
print(x)  # Output will be 20

# -----------------------------------------------------------------------------
# The `global` and `nonlocal` Keywords
# -----------------------------------------------------------------------------
# 1. **`global`**: The `global` keyword allows you to modify a global variable inside a function.
# 2. **`nonlocal`**: The `nonlocal` keyword is used to modify a variable in the **enclosing (non-global) scope**.
#    It is helpful when you want to modify a variable in an outer function’s scope from an inner function.

# Example with `nonlocal`:


def outer():
    x = 10  # Enclosing variable

    def inner():
        nonlocal x  # Modify the enclosing 'x'
        x = 20

    inner()
    print(x)  # Output will be 20


outer()

# =============================================================================
# Scope of Lambda Functions
# =============================================================================
# Lambda functions are **anonymous functions** defined using the `lambda` keyword.
# They also follow the LEGB rule for variable lookup.

# Example:
x = 5  # Global x


def outer():
    x = 10  # Enclosing x
    def my_lambda(): return x  # Lambda function using enclosing x
    return my_lambda()


print(outer())  # Output will be 10, as the lambda accesses the enclosing x

# =============================================================================
# Final Code Summary: Demonstrating Scopes and Namespaces
# =============================================================================
# Here's a summary with all the concepts we’ve discussed.

x = 10  # Global x


def outer():
    x = 20  # Enclosing x
    print(f"Outer x: {x}")  # This prints the 'x' in the enclosing scope

    def inner():
        x = 30  # Local x
        print(f"Inner x: {x}")  # This prints the 'x' in the local scope

    inner()


outer()

# Output:
# Outer x: 20
# Inner x: 30

# =============================================================================
# Key Takeaways:
# =============================================================================
# 1. **Namespaces** are containers where variable names are mapped to objects (values).
# 2. **Scopes** define where these namespaces are accessible within a program.
# 3. **LEGB Rule**:
#    - Local -> Enclosing -> Global -> Built-in.
#    - Python searches for variables in this order when trying to resolve names.
# 4. **Global Variables**: Declared outside any function and can be accessed across functions.
# 5. **Local Variables**: Declared within a function and can only be accessed inside that function.
# 6. **Enclosing Variables**: Variables from an outer function that can be accessed by inner functions.
# 7. **Built-in Variables**: The predefined Python functions and objects.
# 8. **The `global` keyword** is used to modify global variables inside functions.
# 9. **The `nonlocal` keyword** is used to modify variables in an enclosing (non-global) scope.
# =============================================================================
