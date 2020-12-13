number = int(input("Enter number( 0 stop program)"))

positive_counter = 0
negative_counter = 0

while number != 0:
    if number > 0:
        positive_counter += 1
    else:
        negative_counter += 1

    number = int(input("Enter number( 0 stop program)"))
    pass

print("positives", positive_counter)
print("negatives", negative_counter)