import random


def extended_euclid(x, y):
    a2 = 1
    a1 = 0
    b2 = 0
    b1 = 1
    while y != 0:
        q = x // y
        r = x - q * y
        a = a2 - q * a1
        b = b2 - q * b1
        x = y
        y = r 
        a2 = a1
        a1 = a
        b2 = b1
        b1 = b
        m = x 
    a = a2 
    b = b2
    return m, a, b


def test_M_R(n):
    if n < 5 or n % 2 == 0:
        raise ValueError('Неправильное число')
    l = n - 1
    r = 1
    s = 0
    while l != 1:
        if l % 2 == 0:
            l = l // 2
            s = s + 1
        else:
            r = l
            break
    a = random.randint(2, n-2)
    y = (pow(a, r)) % n
    if y != 1 and y != n-1:
        j = 1
        if j <= s - 1 and y != n-1:
            y = (y * y) % n
            if y == 1:
                print('Число', n,'составное')
                return 0
            j = j + 1
        if y != n - 1:
            print('Число', n,'составное')
            return 0
    print('Число', n, 'вероятно простое')
    return 1  


def bin_to_dec(data):
    number = 0
    len_dat = len(data)
    for i in range(0, len_dat):
        number += int(data[i]) * (2**(len_dat - i - 1))
    return number


def simple_gen_k(k, t):
    while True:
        j = k - 1
        mass_p = []
        mass_p.append(1)
        while j > 1:
            b = random.randint(0, 1)
            mass_p.append(b)
            j = j - 1
        mass_p.append(1)
        print(mass_p)
        string = ''
        for i in range(0, len(mass_p)):
            string = string + str(mass_p[i])
        p = bin_to_dec(string)
        i = 1
        x = 0
        while i < t:
            if int(p) % 2 == 0:
                break
            x = test_M_R(int(p))
            if x == 1:
                i = i + 1
            elif x == 0:
                break
        if i == t:
            print(p)
            return p


if __name__ == "__main__":
    pass