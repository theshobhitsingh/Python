age = int(input("Kindly enter your age: "))
day = input("Enter the day: ").strip().capitalize()

ticket_cost_for_children = 8
ticket_cost_for_adults = 12

if age < 18:
    if day == "Wednesday":
        ticket_price = ticket_cost_for_children - 2
    else:
        ticket_price = ticket_cost_for_children
    print(
        f'You are a Child; You need to pay ${ticket_price} for the Movie Ticket')
else:
    if day == "Wednesday":
        ticket_price = ticket_cost_for_adults - 2
    else:
        ticket_price = ticket_cost_for_adults
    print(
        f'You are an Adult; You need to pay ${ticket_price} for the Movie Ticket')