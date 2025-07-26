cars = [
    "Toyota", "Honda", "Ford", "BMW", "Toyota",
    "Tesla", "Ford", "Mercedes", "Honda", "BMW",
    "Hyundai", "Tesla", "Chevrolet", "Chevrolet"
]

seen = set()

for car in cars:
    if car in seen:
        print("Duplicate Found:", car)
        break
    seen.add(car)