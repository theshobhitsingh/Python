password = input("Enter your Password: ")
password_length = len(password)

if password_length < 6:
    print("Your password is Weak!")
elif password_length > 6 and password_length <= 10:
    print("Your password is Medium!")
else:
    print("Your password is Strong!")