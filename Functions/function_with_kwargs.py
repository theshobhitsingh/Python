# Define a function that accepts keyword arguments
def print_kwargs(**kwargs):
    """
    This function accepts a variable number of keyword arguments and prints each key-value pair.

    Parameters:
    **kwargs: A variable number of keyword arguments (key-value pairs).
    """
    # Iterate over the keyword arguments and print each key-value pair
    for key, value in kwargs.items():
        print(f'{key} : {value}')


# Calling the function with different sets of keyword arguments
print("Call 1:")
print_kwargs(Name="IronMan", Power="Superhero")
# Output: Name : IronMan, Power : Superhero

print("\nCall 2:")
print_kwargs(Weapon="Laser", Speed="Fast", Strength="High")
# Output: Weapon : Laser, Speed : Fast, Strength : High

print("\nCall 3:")
print_kwargs(Planet="Earth", Hero="Spiderman")
# Output: Planet : Earth, Hero : Spiderman

print("\nCall 4:")
print_kwargs(Suit="Nano", Power_Level="Advanced", Location="New York")
# Output: Suit : Nano, Power_Level : Advanced, Location : New York

print("\nCall 5:")
print_kwargs(Weapon="Shield", Hero="Captain America",
             Motto="I can do this all day")
# Output: Weapon : Shield, Hero : Captain America, Motto : I can do this all day

print("\nCall 6:")
print_kwargs(Gadgets="Various", Allies=["Thor", "Hulk", "Black Widow"])
# Output: Gadgets : Various, Allies : ['Thor', 'Hulk', 'Black Widow']
