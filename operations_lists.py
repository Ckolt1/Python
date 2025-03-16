seats = list(range(1, 21))
# The end of the range is 21 because range stops at the number before the one you choose.
while True:

    print("Available seats:", seats)

    try:
        seat_choice = int(
            input("Enter the seat number you want to purchase (0 to exit): "))

        if seat_choice not in seats:
            print(
                "This seat has been sold. Try again.")

        if seat_choice == 0:
            print("Thank you for using the ticket system.")
            break
        else:
            seats.remove(seat_choice)
            print(f"Seat {seat_choice} has been successfully purchased!")

    except ValueError:
        print("Please enter a valid number.")
