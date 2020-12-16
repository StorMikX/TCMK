import random
import math
from decimal import Decimal, getcontext


def func(x, n):
    return (x**2 + 1) % n


def nod_euclid(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def ro_pollard():
    n = int(input('Введите число n: \n'))
    c = random.randint(1, 1000)
    #print(c)
    a = c
    b = c
    flag = True
    while flag:
        a = func(a, n)
        #print (a)
        b = func(b, n)
        #print(b)
        b = func(b, n)
        #print (b)
        z = a - b
        d = nod_euclid(z, n)
        #print(d)
        if d == n:
            print("Делитель не найден")
            flag = False
        elif d == 1:
            continue
        else:
            p = d
            print("Нетривиальный делитель:", p)
            flag = False



def ro_1_pollard():
    getcontext().prec = 2
    n = int(input('Введите число n: \n'))

    basefact = []
    with open('BaseFactr.txt', 'r') as Base:
        for line in Base:
            basefact.append(int(line.strip('\n')))
    #print(basefact)
    #[int(x) for x in line.split('\t')

    a = random.randint(2, n-2)
    flag = True
    while flag:
        d = nod_euclid(a, n)
        if d >= 2:
            p = d
            print('Нетривиальный делитель:', p)
            flag = False
        else:
            for simple in basefact:
                n_log = math.log(n)
                p_log = math.log(simple)
                l = int(n_log / p_log)

                a1 = pow(simple, l)
                a = pow(a, a1) % n
            z = a - 1    
            d = nod_euclid(z, n)
            if d == 1 or d == n:
                print('Делитель не найден')
                flag = False
            else:
                p = d
                print('Нетривиальный делитель:', p)
                break
                    #print(l)
           
if __name__ == "__main__":
    ro_1_pollard()
    
