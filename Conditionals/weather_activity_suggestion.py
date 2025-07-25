weather = input("Enter the current weather: ").lower()

if weather == 'sunny':
    print('Go for a Walk!')
elif weather == 'rainy':
    print('Read a Book')
elif weather == 'snowy':
    print("Build a Snowman")
else:
    print("Do what you feel like!")