fruit = input("Enter your favourite fruit: ").strip().capitalize()
fruit_color = input("Enter the color of your fruit: ").strip().lower()

if fruit_color == "green":
    print(f'Your {fruit} is still unripened.')
elif fruit_color == "yellow":
    print(f'Your {fruit} is perfectly ripened.')
else:
    print(f'Your {fruit} is overripe.')