import random

def int_rand_numbers(file):
    with open('file1.txt', 'w') as file:
        for i in range(10):
            file.write(str(random.randint(1, 10)))


def sort_list(num):
    with open('file1.txt','r+') as f:
        num = " ".join(map(str,sorted(f.read())))
    with open('file1.txt','w') as f:   
        f.write(str(num))


sort_list(int_rand_numbers('file'))