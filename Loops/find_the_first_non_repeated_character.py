input_string = input("Enter your String: ")

for char in input_string:
    if input_string.count(char) == 1:
        print("The first non-repeated character is: ", char)
        break