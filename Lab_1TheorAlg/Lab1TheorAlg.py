import random
import math

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


def FastExponentiation_A(a, n):
    #Алгоритм быстрого возведения в степень
    x = 1
    while n:
        if n & 0x01:    #Пока бит n будет равен 1
            x = x * a
        a = a * a
        n >>= 1   #Сдвиг бита вправо(деление числа на 2)
    print(x)
    return x


def FastExponentiationMod_B(a, n, m):
    #Алгоритм быстрого возведения в степень по модулю числа
    x = 1
    while n:
        if n & 0x01:
            x = (x * a) % m
        a = (a * a) % m
        n >>= 1
    print(x)
    return x


def Symbol_Jacobi(a, n):
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
    print('Символ Якоби:', g)
    return g

        
def test_Ferma(a, n):
    if n < 5:
        raise ValueError('n должно быть >= 5')
    if a > (n-2) or a < 2:
        raise ValueError('a должно быть 2 <= a <= (n - 2)')
    #a = random.randint(2, n - 2)
    if n % 2 == 0:
        print("Число n должно быть нечетным!!!")
    else:
        r = pow(a, (n - 1)) % n
        if r == 1:
            print('Число вероятно простое:', n)
        else:
            print('Число составное:', n)
    

def test_S_SHT(n):
    if n < 5:
        raise ValueError('n должно быть >= 5')
    a = (random.randint(2, n - 2))
    r = ((a ** ((n-1)//2)) % n)
    if r != 1 and r != n - 1:
        print('Число', n, 'составное')
        return 0
    s = Symbol_Jacobi(a, n)
    if r % n == s:
        print('Число', n, 'вероятно, простое')
        return 0
    else:
        print('Число', n, 'составное')
        return 0

    
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


def srav_1():
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


def srav_2(p, a, N):
    r1 = Symbol_Jacobi(a, p)
    r2 = Symbol_Jacobi(N, p)
    if r1 != 1 and r2 != -1:
        raise ValueError('Символ Якоби должен быть = 1')
    h = 1
    k = 0
    l = p - 1
    if l % 2 == 0:
        while l % 2 == 0:
            l = l // 2
            k = k + 1
        if l % 2 != 0:
            h = l  
    else:
        h = l
    a1 = pow(a, ((h + 1) / 2))
    a1 = a1 % p
    a2 = pow(a, -1)
    a2 = a2 % p
    N1 = pow(N, h) 
    N1 = N1 % p
    N2 = 1
    j = 0
    for i in range(0, k - 2):
        b = (a1 * N2) % p
        c = (a2 * (b ** 2)) % p
        t = pow(2, (k - 2 - i))
        d = pow(c, t) % p
        if d == 1:
            j = 0
        elif d == -1:
            j = 1
        m = ((2 ** i) * j)
        N2 = N2 * (N1 ** m) % p
    result1 = (a1 * N2) % p
    result=list()
    result.append(a1)
    result.append(N2)
    print("+-", result1)
    print(result)


def sys_srav(b, m):
    M = 1
    x = 0
    for x in range(0, len(m)):
        M = M * m[x]
    for j in range(1, len(m)):
        Mj = M / m[j]
        Nj = (1 / Mj) % m[j]
        x += (b[j] * Nj * Mj) % M
    return x


if __name__ == "__main__":
    pro = True
    while pro:
        knopka = int(input("\t---Выберете алгоритм---\n1) Обобщенный(расширенный) алгоритм Евклида\n"
        "2) Алгоритм быстрого возведения в степень\n"
        "3) Алгоритм быстрого возведения в степень по модулю\n"
        "4) Вычисление символа Якоби\n"
        "5) Тест Ферма\n"
        "6) Тест Соловэя-Штрассена\n"
        "7) Тест Миллера-Рабина\n"
        "8) Генерация простого числа заданной размерности\n"
        "9) Решение сравнения первой степени\n"
        "10) Решение сравнения второй степени\n"
        "11) Решение системы сравнений\n" ))
        if knopka >= 1 and knopka < 12:
            if knopka == 1:
                x = int(input("Введите число x: "))
                y = int(input("Введите число y: "))
                flag_Evklid = True
                while(flag_Evklid):
                    if x >= y:
                        break
                    else:
                        x = int(input("Введите число x >= y\n "))
                        y= int (input("Введите число y <= x\n "))
                print(EuclidAlgorithm(x,y))
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 2:
                a = int(input("Введите число a: "))
                n = int(input("Введите число n: "))
                continue_flag = True
                while continue_flag:
                    if n>=2:
                        break
                    else:
                        n=int(input("Введите число n>=2\n "))
                FastExponentiation_A(a, n)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 3:
                a = int(input("Введите число a: "))
                n = int(input("Введите степень n: "))
                m = int(input("Введите модуль m: "))
                flag = True
                while flag:
                    if a >= 0 and n >= 0 and m >= 0:
                        break
                    else:
                        a = int(input("Введите число a:"))
                        n = int(input("Введите степень n: "))
                        m = int(input("Введите модуль m: "))
                FastExponentiationMod_B(a, n, m)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 4:
                n = int(input("Введите число n, - нечетное целое число n >= 3: "))
                a = int(input("Введите число а, а - целое число 0 <= a < n: "))
                flag = True
                while(flag):
                    if n > a and n >= 3 and a >= 0 and n % 2 != 0:
                        break
                    else:
                        a = int(input("Введите число a, 0 <= a < n: "))
                        n = int(input("Введите число n, n >= 3: "))
                k = Symbol_Jacobi(a, n)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 5:
                n = int(input("Введите нечетное число n, которое больше или равно 5: \n"))
                a = int(input("Введите случайное число a, которое 2 <= a <= n-2: \n"))
                flag = True
                while flag:
                    if n >= 5 and n % 2 != 0:
                        break
                    else:
                        n = int(input("Введите нечетное число n, которое больше или равно 5: \n"))
                test_Ferma(a, n)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 6:
                n = int(input("Введите нечетное число, которое больше или равно 5: \n"))
                flag = True
                while flag:
                    if n >= 5 and n % 2 != 0:
                        break
                    else:
                        n = int(input("Введите нечетное число n, которое больше или равно 5: \n"))
                test_S_SHT(n)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 7:
                n = int(input('Введите нечетное число, которое больше или равно 5: \n'))
                flag = True
                while flag:
                    if n >= 5 and n % 2 != 0:
                        break
                    else:
                        n = int(input("Введите нечетное число n, которое больше или равно 5: \n"))
                test_M_R(n)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 8:
                k = int(input("Введите разрядность k: \n"))
                t = int(input("Введите число итераций t: \n"))
                flag = True
                while flag:
                    if k >= 1 and t >= 1:
                        break
                    else:
                        k = int(input("Введите разрядность k: \n"))
                        t = int(input("Введите число итераций: \n"))
                simple_gen_k(k, t)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 9:
                srav_1()
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 10:
                print('Cравнение вида x*x = a mod p\n')
                p = int(input('Введите число p != 2:'))
                a = int(input('Введите число a >= 0:'))
                N = int(input('Введите число N >= 0:'))
                srav_2(p, a, N)
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
            if knopka == 11:
                x = int(input("Введите число строк савнений (четное): "))
                while True:
                    if x % 2==0:
                        break
                    else:
                        x = int(input("Введите число строк савнений (четное): "))
                b_list = list()
                mod_list = list()
                for x in range(1, x):
                    b_list.append(input("Enter b",x," "))
                    mod_list.append(input("Enter m",x," "))
                while True:
                    for x in range(0, len(mod_list) - 1):
                        if EuclidAlgorithm(mod_list[x], mod_list[x + 1]) == 1:
                            if x+1==len(mod_list):
                                break
                        else:
                            break
                    for x in range(1, x):
                        mod_list.append(input("Enter m",x," "))
                print("Результат = ", sys_srav(b_list, mod_list))
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    pro = False
        else:
            print("\nСделайте правильный выбор!!!\n")        