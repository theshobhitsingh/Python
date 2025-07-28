# lambda_functions_example.py
# This file demonstrates different use cases of lambda functions in Python
# Lambda functions are small anonymous functions defined using the `lambda` keyword.

from functools import reduce

# 1. Simple Lambda Function to Add Two Numbers


def add(x, y): return x + y


# Calling the lambda function to add 5 and 3
print("1. Addition of 5 and 3 using lambda:", add(5, 3))  # Output will be 8


# 2. Using Lambda with `sorted()` to Sort a List of Tuples by the Second Element
data = [(1, 2), (3, 1), (5, 0), (4, 2)]

# Using sorted() with a lambda function as the key to sort the tuples by the second element
sorted_data = sorted(data, key=lambda x: x[1])

# Printing the sorted data
print("\n2. Sorted data by the second element of each tuple:")
print(sorted_data)  # Output will be: [(5, 0), (3, 1), (1, 2), (4, 2)]


# 3. Using Lambda with `map()` to Square Each Number in a List
numbers = [1, 2, 3, 4, 5]

# Using `map()` with a lambda function to square each number in the list
squared_numbers = map(lambda x: x ** 2, numbers)

# Converting the result to a list and printing the squared numbers
print("\n3. Squared numbers using lambda and map:")
print(list(squared_numbers))  # Output will be: [1, 4, 9, 16, 25]


# 4. Using Lambda with `filter()` to Filter Out Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using `filter()` with a lambda function to filter only the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Converting the result to a list and printing the even numbers
print("\n4. Filtered even numbers using lambda and filter:")
print(list(even_numbers))  # Output will be: [2, 4, 6, 8, 10]


# 5. Using Lambda with `reduce()` to Calculate the Cumulative Sum of a List
numbers = [1, 2, 3, 4, 5]

# Using `reduce()` with a lambda function to calculate the cumulative sum
cumulative_sum = reduce(lambda x, y: x + y, numbers)

# Printing the cumulative sum
print("\n5. Cumulative sum of numbers using lambda and reduce:")
print(cumulative_sum)  # Output will be: 15


# 6. Using Lambda to Create a Simple Function Inside a Function
def create_square_function():
    return lambda x: x ** 2


square_function = create_square_function()

print("\n6. Using a lambda function returned from another function:")
print(square_function(7))  # Output will be: 49


# 7. Lambda Function in a Conditional Expression
def max_number(x, y): return x if x > y else y


print("\n7. Larger of two numbers using lambda:")
print(max_number(10, 20))  # Output will be: 20


# 8. Using Lambda with `sorted()` for Custom Sorting by String Length
words = ["apple", "banana", "kiwi", "cherry", "pear"]

sorted_words = sorted(words, key=lambda word: len(word))

print("\n8. Words sorted by length using lambda and sorted:")
# Output will be: ['kiwi', 'pear', 'apple', 'banana', 'cherry']
print(sorted_words)


# 9. Lambda with Multiple Arguments for Concatenating Strings
def concat_strings(s1, s2): return s1 + " " + s2


print("\n9. Concatenating two strings using lambda:")
print(concat_strings("Hello", "World"))  # Output will be: "Hello World"


# 10. Simple Lambda Function to Calculate the Cube of a Number
# A lambda function that calculates the cube of a number.
def cube(x): return x ** 3


# Calling the lambda function to calculate the cube of 3
print("\n10. Cube of 3 using lambda:")
print(cube(3))  # Output will be: 27
