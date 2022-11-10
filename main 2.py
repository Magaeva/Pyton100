 # TODO написать функцию для получения списка уникальных целых чисел

import random
def unique_numbers():
    list_unique_numbers= [random.randint (-10,10) for x in range(15)]
    list_unique_numbers=[]
    while len (list_unique_numbers)>16:
        x=random.randint (-10,10)
        if x not in list_unique_numbers:
            list_unique_numbers.append(x)
    return list_unique_numbers
print(unique_numbers)

