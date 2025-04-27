class Pet:
    vet_name = "Animal Clinic"
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name

        self.__owner_last_name = owner_last_name

        self.__pet_id = pet_id

        self.__pet_name = pet_name

        self.__pet_type = pet_type

    def get_owner_first_name(self):

        return self.__owner_first_name

    def set_owner_first_name(self, name):

        self.__owner_first_name = name

    def get_owner_last_name(self):

        return self.__owner_last_name

    def set_owner_last_name(self, name):

        self.__owner_last_name = name

    def get_pet_id(self):

        return self.__pet_id

    def set_pet_id(self, pet_id):

        self.__pet_id = pet_id

    def get_pet_name(self):

        return self.__pet_name

    def set_pet_name(self, name):
        self.__pet_name = name

    def get_pet_type(self):

        return self.__pet_type

    def set_pet_type(self, pet_type):

        self.__pet_type = pet_type

    def display_pet_info(self):

        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")

        print(f"Pet ID: {self.__pet_id}")

        print(f"Pet Name: {self.__pet_name}")

        print(f"Pet Type: {self.__pet_type}")

        print(f"Vet Name: {Pet.vet_name}")

# pet 1 does not need a defined animal because its default set to dog
pet1 = Pet("Bob", "Smith", 1, "Sparky")

pet2 = Pet("Jane", "Doe", 2, "Butters", "Cat")

pet3 = Pet("John", "Doe", 3, "FISHRON", "Fish")

# this should test setter function and overide Sparky name
pet1.set_pet_name("Sparkles")

print("Pet information")
pet1.display_pet_info()

pet2.display_pet_info()

pet3.display_pet_info()


def check_property(pet, prop_name):

    return hasattr(pet, prop_name)

print("Property Checks")

print("pet1 has '__pet_name':", check_property(pet1, '_Pet__pet_name'))

print("pet3 has 'set_pet_id':", check_property(pet3, 'set_pet_id'))

