import math


def circle(radius):
    area = math.pi * (radius ** 2)  # Area = π * radius^2
    circumference = 2 * math.pi * radius  # Circumference = 2 * π * radius
    return area, circumference


# Ask the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Get area and circumference
area, circumference = circle(radius)

# Print the results
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
