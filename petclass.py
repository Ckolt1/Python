class Pet:
    def __init__(self, kind, breed, name):

        self.__kind = kind

        self.__breed = breed

        self.__name = name


    def get_kind(self):

        return self.__kind

    def get_breed(self):

        return self.__breed

    def get_name(self):

        return self.__name

    def set_kind(self, kind):

        self.__kind = kind

    def set_breed(self, breed):

        self.__breed = breed

    def set_name(self, name):

        self.__name = name

    def print_details(self):
        print(f"Pet Name: {self.__name}")

        print(f"Pet Kind: {self.__kind}")

        print(f"Pet Breed: {self.__breed}")


pet1 = Pet("Cat", "House Cat", "Butters")

pet2 = Pet("Dog", "Pug", "Stout")

pet3 = Pet("Fish", "Bass", "Bubbles")

print("Here Are The Pet Details:")

pet1.print_details()

pet2.print_details()

pet3.print_details()

# choose 3 demonstration
# 1 __name__
print("The name of the class is: ", Pet.__name__)

# 2 isinstance()
print("Pet 1 is an instance of the pet class: ", isinstance(pet1, Pet))

# 3 type()
print("The type of class used to instantiate a pet object is: ", type(pet1))


