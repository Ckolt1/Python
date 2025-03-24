def factorial(n):
    # n is the placeholder fro the integer
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    
def main():
    integer = int(input("Enter a postive number: "))
    result = factorial(integer)
    print(f"The factorial of {integer} is {result}.")
    # the main down here is what calls the program
main()