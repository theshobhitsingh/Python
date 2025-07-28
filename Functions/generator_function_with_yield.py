# # Function to print even numbers up to a specified limit
# def even_number_generator(limit):
#     for i in range(2, limit + 1, 2):  # Start from 2 and go up to 'limit'
#         print(i)

# # Calling the function
# even_number_generator(100)  # This will print even numbers from 2 to 100


# Function to generate even numbers up to a specified limit using yield
def even_number_generator(limit):
    """
    This function generates even numbers from 2 up to a specified limit.
    The function uses `yield` to return each even number one at a time.

    Parameters:
    limit (int): The upper limit up to which even numbers should be generated.

    Yields:
    int: The next even number in the sequence.
    """
    # Iterate from 2 to the limit, stepping by 2 (even numbers)
    for i in range(2, limit + 1, 2):
        yield i  # Yield the next even number


# Calling the generator function and printing the even numbers one by one
for even_number in even_number_generator(100):
    print(even_number)


# Benefits of yield:
# 1. Memory Efficiency:
# With yield, the function does not generate all the even numbers at once. It yields the values one by one.

# This makes the function memory-efficient since it doesn’t create a large list of values in memory. Instead of holding all values at once, only one value is in memory at any given moment.

# Example: If we generate even numbers up to 1,000,000, using yield ensures that we don’t hold a list of all those numbers in memory — we only generate one number at a time when needed.

# 2. Lazy Evaluation:
# yield allows for lazy evaluation. This means that values are not computed upfront. Instead, they are computed only when requested (when next() is called or in a for loop).

# Why is this useful? This is particularly helpful when working with large datasets or infinite sequences, where it would be inefficient or impossible to store the entire data set in memory.

# Example: If you’re generating numbers from 2 to ∞, you wouldn’t want to store all those numbers at once. yield lets you compute only the numbers as they are needed.

# 3. State Retention:
# The key advantage of yield is that the function remembers its state between calls. Every time the generator function is paused (via yield), Python retains the function's state (the current value of variables, where the function was paused, etc.).

# When the generator is resumed, it continues from the exact point where it was paused.

# Example: In our even number generator, after yielding 2, when the function is called again, it resumes from 4. This eliminates the need to recompute or reset the function, making the iteration efficient.

# When to Use yield:
# 1. When You Want to Generate Values on the Fly (Lazy Evaluation):
# If you need to generate a sequence of values that may be too large to fit in memory all at once (or an infinite sequence), yield is a great tool.

# Example: Generating an infinite series of numbers (e.g., Fibonacci) or working with a huge file that you want to read one line at a time.

# 2. When You Are Working with Large Datasets or Infinite Sequences:
# In scenarios where you don’t want to store a massive list of values in memory, yield allows you to generate and process each value without overwhelming your system.

# Example: Reading a large file line by line and processing each line as it’s read instead of loading the entire file into memory.

# 3. When You Need to Create a Custom Iterator:
# yield is perfect for creating custom iterators. If you need to iterate over a complex dataset or generate a sequence with special rules, a generator is an ideal solution.

# Example: You could create a generator to traverse a tree, a graph, or any other data structure, yielding values as needed without needing to build a separate iterator class.

# Summary of yield:
# Memory Efficient: No need to store entire lists of data.

# Lazy Evaluation: Values are computed only when required.

# State Retention: The function “remembers” where it left off.

# Use yield when you need performance, memory efficiency, and convenience in iterating over large datasets or infinite sequences.
