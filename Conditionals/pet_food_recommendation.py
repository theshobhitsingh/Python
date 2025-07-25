pet = input("Enter your pet (Dog, Cat, etc.): ").strip().capitalize()
pet_age = int(input("Enter the age of your pet: "))

# Check if the pet is a Dog under 2 years old
if pet_age < 2 and pet.lower() == "dog":
    print(f'{pet} needs Baby Dog food')

# Check if the pet is a Dog (not a puppy)
elif pet.lower() == "dog":
    print(f'{pet} needs regular Dog food')

# Check if the pet is a Cat under 2 years old
elif pet_age < 2 and pet.lower() == "cat":
    print(f'{pet} needs Kitten food')

# Check if the pet is a Cat (not a kitten)
elif pet.lower() == "cat":
    print(f'{pet} needs regular Cat food')

# For all other pets
else:
    if pet_age < 2:
        print(f'{pet} needs Baby food')
    else:
        print(f'{pet} needs regular pet food')