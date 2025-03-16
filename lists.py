
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

steps = []

for day in days:
    while True:
        step_count = int(
            input(f"Enter the number of steps taken on {day}: "))
        if step_count < 0:
            print("Please enter a number.")
        else:
            steps.append(step_count)
        break


print("You took:")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")

final_steps = sum(steps)

print(f"Total steps you took during the week: {final_steps}")

av_steps = final_steps / 7
print(f"You took {av_steps} steps each day")
