import random

my_list = []

for i in range(0, 10):
    my_list.append(random.randint(1, 1000))
    pass

print("My list is: ", my_list)
print("max:", max(my_list))
print("min:", min(my_list))