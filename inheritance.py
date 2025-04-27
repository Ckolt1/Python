class Employee:
    def __init__(self, name, number):

        self.__name = name

        self.__number = number

    def get_name(self):

        return self.__name

    def get_number(self):

        return self.__number

    def set_name(self, name):

        self.__name = name

    def set_number(self, number):

        self.__number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):

        super().__init__(name, number)

        self.__shift_number = shift_number

        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):

        return self.__shift_number
    
    def get_shift_name(self):
        
        return "Day" if self.__shift_number == 1 else "Night"

    def get_hourly_pay_rate(self):

        return self.__hourly_pay_rate

    def set_shift_number(self, shift_number):

        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, pay_rate):

        self.__hourly_pay_rate = pay_rate

def main():
# ENTER
    name = input("Enter the employee name: ")

    number = input("Enter the employee number: ")

    shift = int(input("Enter the shift number (1 = Day, 2 = Night): "))

    pay_rate = float(input("Enter their hourly pay rate: $"))

    #WORKER
    worker = ProductionWorker(name, number, shift, pay_rate)

# DISPLAY
    print("\nEmployee Info:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    # Shift kept displaying as 1 or 2 until i set it to either day or night
    print("Shift:", worker.get_shift_name())
    print("Pay Rate:$ ", format(worker.get_hourly_pay_rate(), ".3f"))

main()