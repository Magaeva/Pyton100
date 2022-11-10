import random
def get_random_password(x):
    chlist=list (map(chr, range(ord('a'), ord('z')+1)))+list (map(chr,range (ord('A'), ord('Z')+1)))+list(map(chr, range(ord('0'), ord ('9')+1)))# TODO написать функцию генерации случайных паролей
    return ''. join(random.sample(chlist,x))
print(get_random_password(10))

