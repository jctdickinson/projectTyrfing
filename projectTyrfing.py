import random

def generate_list(list_size):
    a_list = []
    for i in range(list_size):
        a_list.append(random.randint(0, 99))
    return a_list


print(generate_list(10))