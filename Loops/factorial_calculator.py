number = int(input("Enter the number: "))
factorial = 1

while number != 0:
    factorial = factorial * number
    number = number - 1

print('The Factorial is: ', factorial)