calculate = "calculations"

while True:
    calculate = input("Give (S) for sum or (A) for average")
    if calculate is "S" or calculate is "A":
        break
        pass
    pass

i = 0
sum = 0

if calculate is "S":
    for i in range(1, 11):
        sum = sum + i
        pass
    print(sum)
    pass

elif calculate is "A":
    while i < 11:
        sum = sum + i
        i += 1
        pass
    average = sum / 10
    print(average)