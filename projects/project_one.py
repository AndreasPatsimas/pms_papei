dicti = dict()

try:
    with open("C:/Directory1/sample-text-file.txt", mode="r") as my_file:
        my_list = []
        for line in my_file.readlines():
            my_list = line.split()
            for word in my_list:
                if word not in dicti:
                    dicti[word] = 1
                else:
                    dicti[word] += 1
        print(dicti)
except FileNotFoundError as err:
    print("File not found")
    raise err