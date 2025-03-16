
total = 0
average = 0
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

for time in time_slots:
    heart_rate = input(f"Enter your heart rate (BPM) for {time}: ")
    heart_rates.append([time, heart_rate])

print("Your Heart Rate Were")
for i in range(4):
    time = heart_rates[i][0]
    heart_rate = heart_rates[i][1]
    total += int(heart_rate)
    print(f"At {time} your heart rate BPM were: {heart_rate}")

average = total / 4
print(f"\nYour average heart rate BPM was {average:.1f} today")
