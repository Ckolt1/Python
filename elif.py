grade = float(input("Please enter your grade number : "))

if grade < 0 or grade > 100:
    print("Please enter a number between 0 and 100.")

else:
    if grade >= 90:
        letter = 'A'

    elif grade >= 80:
        letter = 'B'

    elif grade >= 70:
        letter = 'C'

    elif grade >= 60:
        letter = 'D'

    elif grade >= 0:
        letter = 'F'

    print(f"Your letter grade is: {letter}")
