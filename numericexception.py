class NotNumericError(Exception):
    def __init__(self, message):

        self.message = message

        super().__init__(self.message)

def main():

    try:
        user_input = input("Please enter a number: ")

        if not user_input.isnumeric():

            raise NotNumericError("Error, Input must be a numeric value.")
        
    except NotNumericError:

        print("Error, Input must be a numeric value.")
    else:

        print("You entered a valid numeric value:", user_input)
        return True  
    finally:

        print("End of Code.\n")
        
main()