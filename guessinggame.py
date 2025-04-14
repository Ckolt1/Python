
# imports a rando number
import random

def main():
    random_number = random.randint(1, 100)
    guess = None

    print("Guess a number inbetween 1 - 100")
# != means not equal to, == means equal to <= means less than or equal to
    while guess != random_number:
        
        guess = int(input("Enter your guess: "))
# abs is for finding absolute value
        difference = abs(random_number - guess
)
        if guess == random_number:
            print("You guessed Right!")
        else:
                
            if difference <= 5:

                print("Very Hot")

            elif difference <= 15:

                print("Hot")

            elif difference <= 25:

                print("Cool")

            else:

                print("Cold")
main()
