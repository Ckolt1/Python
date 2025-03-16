names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]

print("Sorted names:")

print(names)

names.reverse()

print("Reversed sorted names:")

print(names)
