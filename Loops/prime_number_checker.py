number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not a Prime Number")
else:
    for num in range(2, number):
        if number % num == 0:
            print(number, "is not a Prime Number")
            break
    else:
        print(number, "is a Prime Number")