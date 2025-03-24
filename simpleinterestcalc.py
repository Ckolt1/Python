def calculate_interest(principal, rate, time):
    # Simple Interest = (Principal Amount × Rate of Interest × Time) / 100
    interest = (principal * rate * time) / 100
    return interest
# had to use float or else they would be seen as a string
principal = float(input("Enter the principal: "))
rate = float(input("Enter the  interest rate (%): ")) 
time = float(input("Enter the time period: "))

interest = calculate_interest(principal, rate, time)
print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")