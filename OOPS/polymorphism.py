# Parent Class (Super Class)
class Animal:
    def speak(self):
        return "The animal makes a sound"

# Child Class 1


class Dog(Animal):
    def speak(self):
        return "Woof!"

# Child Class 2


class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function that demonstrates polymorphism


def animal_sound(animal):
    # The same function behaves differently based on the object passed to it
    print(animal.speak())


# Creating instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()

# Demonstrating polymorphism
animal_sound(my_dog)  # Output: Woof!
animal_sound(my_cat)  # Output: Meow!