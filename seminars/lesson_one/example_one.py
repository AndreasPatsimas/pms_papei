number_one = int(input("Give me first number"))

number_two = int(input("Give me second number"))

symbol = input("Give symbol")

if symbol is "+":
    print(number_one + number_two)

elif symbol is "-":
    print(number_one - number_two)

elif symbol is "*":
    print(number_one * number_two)

elif symbol is "/":
    print(number_one / number_two)

else:
    print("Wrong symbol")