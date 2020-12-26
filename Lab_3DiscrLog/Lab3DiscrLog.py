import math
import random


def function(a, b, c, p):
    if c < p // 2: 
        c_ = (a * c) % p
    if c >= p // 2:
        c_ = (b * c) % p
    return c_
    

def klog(c, p): 
    if c < p // 2: 
        sr = 0
    if c >= p // 2:
        sr = 1
    return sr


def EuclidAlgorithm(x, y):
    """Алгоритм нахождения НОД двух чисел"""
    a1 = 0
    a2 = 1
    b1 = 1
    b2 = 0
    if x >= y:
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
        a = a2
        b = b2
    else:
        print("Ошибка: x < y")  
        return 0
    return x


def srav_1(a, b, m):
    d = math.gcd(a, m)
    l = m
    #x = 0
    if d > 1 and b%d != 0:
        print('Решений нет')
    else:
        while b%d == 0:
            if d != 1:
                a = int(a / d)
                b = int(b / d)
                m = int(m / d)
                d = math.gcd(a, m)
            else:
                N = []
                for r in range(l):
                    if (a*r - b)%m == 0:
                        N.append(r)
                #x = min(N)
                break
    return N


def eulers_phi(p):
    #Функция Элера для p
    r = p
    i = 2
    while i * i <= p:
        if p % i == 0:
            while p % i == 0:
                p = p // i
            r = r - r // i
        else:
            i = i + 1
    if p > 1:
        r = r - r // p
    return r 


def divisors_of_a_number(r):
    #Делители числа r
    divisors = [x for x in range (1, r // 2 + 1) if r % x == 0] + [r]          
    return divisors


def order_of_a(a, p, divisors):
    #Вычисление порядка числа а
    vip_ner = list()
    for d in divisors:
        a1 = a ** d % p
        if a1 % p == 1:
            vip_ner.append(d)
        else:
            continue
    order = min(vip_ner)
    return order
    

def discrlog(a, b, p, order):
    #Вычисление x 
    u = 2
    v = 2
    a_1 = a ** u
    b_1 = b ** v
    c = (a_1 * b_1) % p
    d = c
    kc = 0
    kd = 0
    xc = 0
    xd = 0
    flag = True
    while flag:
        if klog(c, p) == 1:
            xc = xc + 1
        else:
            kc = kc + 1
        if klog(d, p) == 1:
            xd = xd + 1
        else:
            kd = kd + 1
        c = function(a, b, c, p)
        d = function(a, b, d, p)
        if klog(d, p) == 1:
            xd = xd + 1
        else: 
            kd = kd + 1
        d = function(a, b, d, p)
        if c % p == d % p:
            flag = False
    xcd = xc - xd
    kcd = kd - kc
    x = srav_1(xcd, kcd, order)
    return x 


def FastExponentiationMod_B(a, n, m):
    #Алгоритм быстрого возведения в степень по модулю числа
    x = 1
    while n:
        if n & 0x01:
            x = (x * a) % m
        a = (a * a) % m
        n >>= 1
    return x


def test_Ferma(n) -> int:
    #Проверка на простату числа                             
    if n < 5:
        raise ValueError('n должно быть >= 5')
    a = random.randint(2, n - 2)
    if n % 2 == 0:
        return 0
    else:
        r = pow(a, (n - 1)) % n
        if r == 1:
            return 1
        else:
            return 0
    

if __name__ == "__main__":
    work = True
    while work:
        print('Введите коэффициенты сравнения вида: a**x = b (mod p)')
        p = int(input('p (простое число): '))
        if test_Ferma(p) == 0:
            work = False
            raise ValueError('Число p должно быть простым!!!')
        a = int(input('a: '))
        b = int(input('b (1 <= b <= p): '))
        if b < 1 or b > p:
            raise ValueError('Число b должно быть в пределе [1, p]')


        r = eulers_phi(p)
        div = divisors_of_a_number(r)
        order = order_of_a(a, p, div)
        x = discrlog(a, b, p, order)
        for i in x:
            res = FastExponentiationMod_B(a, i, p)
            if res % p == b % p:
                print(f'{a}**{i} = {b} (mod {p})')
                print('Решение задачи дискретного логарифмирования:', i)
        #check(a, x, b, p)
        again = input('Хотите повторить программу? (Y, N) \n').lower()
        if again == 'y':
            pass
        else:
            work = False