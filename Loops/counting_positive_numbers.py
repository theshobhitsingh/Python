numbers = [1, -2, 3, 4, 5, -7, -9, 20, -21, 11, -100, 0]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

print(f'Total number of Positives in the list are {positive_number_count}')