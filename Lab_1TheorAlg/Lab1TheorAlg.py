

def EuclidAlgorithm(x, y):

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

def Symbol_Jacobi():
    n = int(input("Введите число n, - нечетное целое число n >= 3: "))
    a = int(input("Введите число а, а - целое число 0 <= a < n: "))
    
    nod = EuclidAlgorithm(n, a)
    g = 1
    
    if nod != 1:
        print('0')
        return 0
    
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
        if a % 4 == n and n % 4 == 3:
            g = -g
        c = a
        a = n % c
        n = c
        
    print('res', g)

        


#def test_Ferma():
#    n = int(input("Введите нечетное число, которое больше или равно 5: \n"))
#    if n < 5:
#        raise ValueError('n должно быть >= 5')
#    a = int(input("Введите случайное число 2 <= a <= (n - 2): \n" ))
#    if a > (n-2) or a < 2:
#        raise ValueError('a должно быть 2 <= a <= (n - 2)')
#
#    if n % 2 == 0:
#        print("Число n должно быть нечетным!!!")
#    else:
#        r = pow(a, (n - 1)) % n
#        if r == 1:
#            print('Число вероятно простое:', n)
#        else:
#            print('Число составное:', n)
    

if __name__ == "__main__":
    Symbol_Jacobi()
    


    
    