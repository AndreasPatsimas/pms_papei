right_choices = ["A", "B", "C", "D"]

def right_choice():
    right_choice = None
    while True:
        right_choice = input("choose the correct answer.")
        if right_choice in right_choices:
            break
            pass
        pass
    pass


correct_answers = 0

try:
    with open("C:/Directory1/mc.tsv", mode="r") as my_file:
        my_list = []
        for line in my_file.readlines():
            my_list.append(line.split("\t"))
            pass

        initial_list = my_list[0]
        my_list.pop(0)
        for question in my_list:
            print(initial_list[0] + ":", question[0], "\n")
            print(initial_list[1], question[1])
            print(initial_list[2], question[2])
            print(initial_list[3], question[3])
            print(initial_list[4], question[4], "\n")
            answer = right_choice()
            if answer is question[5]:
                correct_answers += 1
                print("Correct")
            else:
                print("Incorrect.", "The correct answer is:", question[6])
            pass
        print("your correct answers are:", correct_answers)

except FileNotFoundError as err:
    print("File not found")
    raise err