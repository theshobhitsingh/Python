coffee_size = input(
    "Enter the size of your coffee (Small | Medium | Large): ").strip().upper()
extra_shot_input = input(
    "Do you want an extra shot? (yes/no): ").strip().lower()

extra_shot = extra_shot_input == "yes"

price = 0

if coffee_size == "SMALL":
    price = 2
elif coffee_size == "MEDIUM":
    price = 3
elif coffee_size == "LARGE":
    price = 4
else:
    print("Invalid coffee size selected.")

if extra_shot:
    price += 0.5

if coffee_size in ["SMALL", "MEDIUM", "LARGE"]:
    print(
        f"Your total for a {coffee_size.capitalize()} coffee {'with' if extra_shot else 'without'} an extra shot is: ${price:.2f}")