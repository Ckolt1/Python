# starting code gives error is you use letters instead of numbers

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Error, Use valid NUMBERS")


square_number()
