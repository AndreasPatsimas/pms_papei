import random

choices = ("R", "S", "P")
wins = 0
draws = 0
lose = 0


def winner(user_choice, computer_choice):
    if user_choice is computer_choice:
        return "D"
    elif user_choice is "R" and computer_choice is "S":
        return "W"
    elif user_choice is "R" and computer_choice is "P":
        return "L"
    elif user_choice is "S" and computer_choice is "R":
        return "L"
    elif user_choice is "S" and computer_choice is "P":
        return "W"
    elif user_choice is "P" and computer_choice is "R":
        return "W"
    elif user_choice is "P" and computer_choice is "S":
        return "L"


for i in range(0, 6):
    user_choice = input("R (rock), S (scizor) or P (paper)")
    if user_choice not in choices:
        break
        pass

    computer_choice = choices[random.randint(0, 2)]
    print("User:", user_choice, "Computer:", computer_choice)
    result = winner(user_choice, computer_choice)
    print("The result is:", result)

    if result is "W":
        wins += 1
    elif result is "D":
        draws += 1
    else:
        lose += 1
    pass

print("-------------------------Final Results------------------")
print("W:", wins, "D", draws, "L:", lose)

