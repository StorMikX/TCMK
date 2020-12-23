import random
import math

def EuclidAlgorithm(y, x):

    """Алгоритм нахождения НОД двух чисел"""

    #x = int(input("Введите число x: "))
    #y = int(input("Введите число y: "))

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

        #d = x
        a = a2
        b = b2
        #print("НОД:", d)
        #print("Число а: ", a)
        #print("Число b: ", b)
    else:
        print("Ошибка: x < y")  
        return 0
    return x

#def FastExponentiation_A():
#    #Алгоритм быстрого возведения в степень
#    a = float(input("Введите число a: "))
#    n = int(input("Введите степень n: "))
#    x = 1
#    while n:
#        if n & 0x01:    #Пока бит n будет равен 1
#            x = x * a
#        a = a * a
#        n >>= 1   #Сдвиг бита вправо(деление числа на 2)
#    print(x)

#def FastExponentiationMod_B():
#    #Алгоритм быстрого возведения в степень по модулю числа
#    a = float(input("Введите число a: "))
#    n = int(input("Введите степень n: "))
#    mod = int(input("Введите модуль: "))
#    x = 1
#    while n:
#        if n & 0x01:
#            x = (x * a) % mod
#        a = (a * a) % mod
#        n >>= 1
#    print(x)        

def Symbol_Jacobi(a, n):
    #n = int(input("Введите число n, - нечетное целое число n >= 3: "))
    #a = int(input("Введите число а, а - целое число 0 <= a < n: "))
    
    nod = EuclidAlgorithm(n, a)
    if nod != 1:
        print('0')
        return 0
    
    g = 1
    
    if a < 0:
        a = -a
        if n % 4 == 3:
            g = -g
    while a != 0:
        t = 0
        while a % 2 == 0:
            t = t + 1
            a = a / 2
        if t % 2 != 0:
            if n % 8 == 3 or n % 8 == 5:
                g = -g
        if a % 4 == 3 and n % 4 == 3:
            g = -g
        c = a
        a = n % c
        n = c
        
    #print('res', g)
    return g

        


#def test_Ferma():
#    n = int(input("Введите нечетное число, которое больше или равно 5: \n"))
#    if n < 5:
#        raise ValueError('n должно быть >= 5')
#    a = int(input("Введите случайное число 2 <= a <= (n - 2): \n" ))
#    if a > (n-2) or a < 2:
#        raise ValueError('a должно быть 2 <= a <= (n - 2)')
#
#    #a = random.randint(2, n - 2)
#
#    if n % 2 == 0:
#        print("Число n должно быть нечетным!!!")
#    else:
#        r = pow(a, (n - 1)) % n
#        if r == 1:
#            print('Число вероятно простое:', n)
#        else:
#            print('Число составное:', n)
    

def test_S_SHT():
    n = int(input("Введите нечетное число, которое больше или равно 5: \n"))
    if n < 5:
        raise ValueError('n должно быть >= 5')
    a = (random.randint(2, n - 2))
    #a = int(input('Ведите a'))
    #r = pow(a, (n - 1) / 2) % n
    r = ((a ** ((n-1)//2)) % n)
    
    if r != 1 and r != n - 1:
        print('Число', n, 'составное')
        return 0
    
    s = Symbol_Jacobi(a, n)
    #if (r % n) == (s % n):
    if r % n == s:
        print('Число', n, 'вероятно, простое')
        return 0
    else:
        print('Число', n, 'составное')
        return 0

    
def test_M_R(n):
    #n = int(input('Введите нечетное число, которое больше или равно 5: \n'))
    #if n < 5 or n % 2 == 0:
    #    raise ValueError('Неправильное число')
    
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


def Big_Evklid(a, m):
    a2 = 1
    a1 = 0
    b2 = 0
    b1 = 1
    while m != 0:
        q=int(a / m)
        r=a - q * m
        a=a2 - q * a1
        b=b2 - q * b1
        a = m
        m = r
        a2 = a1
        a1 = a
        b2 = b1
        b1 = b
    a_0=a2
    b=b2
    return a_0


def ReshSrPerStep(a, b, m):
    print('Cравнение вида ax = b mod m\n')
    a = int(input('a: '))
    b = int(input('b: '))
    m = int(input('m: '))
    d = math.gcd(a, m)
    l = m
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
                print('Решения:', N)
                break


if __name__ == "__main__":
    #test_M_R()
    #simple_gen_k(10, 100)
    #test_S_SHT()
    pass


    
    