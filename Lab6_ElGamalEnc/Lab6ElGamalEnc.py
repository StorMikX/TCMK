import random
from math import pow

a = random.randint(2, 10)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)

    return x % c


def encrypt(msg, q, h, g):
    en_msg = []

    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p


def decrypt():
    en_msg = []
    with open('encrypt.txt', 'r') as file:
        file = file.read().split('\n')
        for i in range(len(file) - 1):
            en_msg.append(int(file[i]))
    with open('params.txt', 'r') as file:
        file = file.read().split('\n')
        p = int(file[0])
        key = int(file[1])
        q = int(file[2])
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))
    dmsg = ''.join(dr_msg)
    with open('decrypt.txt', 'w') as file:
        file.write(dmsg)



def main_menu():
    print(
        'Menu:\nЗашифровать - 1\nРасшифровать - 2\nВыход - 0')
    return None


main_menu()
while True:
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        msg = input('Введите текст: ')
        q = random.randint(pow(10, 20), pow(10, 50))
        g = random.randint(2, q)
        key = gen_key(q)
        h = power(g, key, q)
        en_msg, p = encrypt(msg, q, h, g)
        with open('params.txt', 'w') as file:
            file.write(str(p) + '\n' + str(key) + '\n' + str(q))
        with open('encrypt.txt', 'w') as file:
            for i in en_msg:
                file.write(str(i) + '\n')
        print('Текст зашифрован!')
    elif choice == 2:
        decrypt()
        print('Текст расшифрован!')
    elif choice == 0:
        quit()
