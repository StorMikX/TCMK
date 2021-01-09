def EuclidAlgorithm(x, y):
    """Алгоритм нахождения НОД двух чисел"""
    a1 = 0
    a2 = 1
    b1 = 1
    b2 = 0
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


def modinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = EuclidAlgorithm(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


def sys_srav():
    chislosrav = int(input('Введите число сравнений в системе: '))
    b_list = []
    mod_list = []
    for x in range(0, chislosrav):
        b_list.append(int(input("Enter b: ")))
        mod_list.append(int(input("Enter m: ")))
    
    for x in range(0, len(mod_list) - 1):
        if EuclidAlgorithm(mod_list[x], mod_list[x + 1]) == 1:
            if x+1==len(mod_list):
                break
        else:
            break   
    M = 1
    x = 0
    for i in range(0, len(mod_list)):
        M = M * mod_list[i]
    for j in range(len(mod_list)):
        Mj = M / mod_list[j]
        Mj_1 = modinv(Mj, mod_list[j])
        Nj = Mj_1 % mod_list[j]
        #Nj = (1 / Mj) % mod_list[j]
        x += (b_list[j] * Nj * Mj)
        x = x % M
    print(f'Решение системы сравнений: {x}')

#print(EuclidAlgorithm(20, 4))
sys_srav()