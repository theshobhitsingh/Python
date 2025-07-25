distance = int(input("Enter the distance: "))

if distance < 3:
    print("You should walk this distance")
elif distance > 3 and distance <= 15:
    print("You should Take a Bike!")
else:
    print("You should Book a Car!")