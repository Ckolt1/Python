# NUMBERS
n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the Second Number:  "))

# AND
print("AND")
print(
    f"Is number 1 less than 15 and number 2 greater than 66? {n1 < 15 and n2 > 66}")
print(
    f"Is number 1 equal to number 2 and number 2 * 1? {n1 == n2 and n2 * 1}")

# OR
print("OR")
print(
    f"Is number 1 greater than 100 or number 2 less than 50? {n1 > 100 or n2 < 50}")
print(
    f"Is number 1 equal to 0 or number 2 equal to 0? {n1 == 0 or n2 == 0}")

# NOT
print("NOT")
print(
    f"Is it not true that number 1 is less than 0? {not n1 < 0}")
print(
    f"Is it not true that number 2 equals 0? {not n2 == 0}")
