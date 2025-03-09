bottles = 99

while bottles > 0:

    if bottles == 1:
        print(
            f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print(
            "Take one down and pass it around, no more bottles of beer on the wall.\n")

    else:
        print(
            f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(
            f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
# I forgot to subtract bottles at first and found out what an infinite loop was lol
    bottles -= 1
# Print when at the end of bottles
print("No more beer on the wall!")
