days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = []

for i in range (0, 7):
    temperatures.append(float(input("Give highest temperature of day")))
    pass

sum = 0
average = 0

for temperature in temperatures:
    sum += temperature
    pass

average = sum / len(temperatures)

max_temp = max(temperatures)
min_temp = min(temperatures)

max_day = days[temperatures.index(max_temp)]
min_day = days[temperatures.index(min_temp)]

print("Average of temperatures is", average)
print("Max temperature is", max_temp, "on", max_day)
print("Min temperature is", min_temp, "on", min_day)
