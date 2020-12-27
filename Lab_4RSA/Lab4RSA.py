import random
import string
import json
#pylint: disable=E1101

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
    y = (pow(a, r, n)) #% n
    if y != 1 and y != n-1:
        j = 1
        if j <= s - 1 and y != n-1:
            y = (y * y) % n
            if y == 1:
                #print('Число', n,'составное')
                return 0
            j = j + 1
        if y != n - 1:
            #print('Число', n,'составное')
            return 0
    #print('Число', n, 'вероятно простое')
    return 1  


def bin_to_dec(data):
    number = 0
    len_dat = len(data)
    for i in range(0, len_dat):
        number += int(data[i]) * (2**(len_dat - i - 1))
    #print(number)
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
        #print(mass_p)
        string = ''
        for i in range(0, len(mass_p)):
            string = string + str(mass_p[i])
        p = bin_to_dec(string)
        del mass_p
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
            #print(f'p = {p}')
            return p

def rsa_encryption(m, e, n):
    c = pow(m, e, n)
    print(c)
    return int(c)


def rsa_decryption(c, d, n):
    m = pow(c, d, n)
    return m


def oktets():
    pass

    


if __name__ == "__main__":
    work = True
    while work:
        print('\n\t---RSA Menu---\n'
              '1) Генерация параматров ключей\n'
              '2) Шифрование\n'
              '3) Расшифрование')
        choice = (int(input('Выберите функцию программы: ')))
        if choice >= 1 and choice < 4:
            if choice == 1:
                print('\nГенерация параметра p')
                k1 = int(input('Укажите двоичную разрядность числа p: '))
                t1 = int(input('Укажите число итераций генератора числа p: '))
                p = simple_gen_k(k1, t1)
                print(f'p = {p}')
                print('\nГенерация параметра q')
                k2 = int(input('Укажите двоичную разрядность числа q: '))
                t2 =int(input('Укажите число итераций генератора числа q: '))
                q = simple_gen_k(k2, t2)
                print(f'q = {q}')
                n = p * q
                print(f'\nЧисло n = {n}')
                x = (p - 1) * (q - 1)
                gen = True
                while gen:
                    e = int(input('\nВведите число e: '))
                    m, a, b = extended_euclid(x, e)
                    if m != 1:
                        print('Выберите другое значение е')
                        pass
                    else:
                        print('m:', m)
                        gen = False
                d = b
                exponent1 = d % (p - 1)
                exponent2 = d % (q - 1)
                coefficient = pow(q, -1) % n
                OpenKey = {
                    'PublicKey': 
                    {
                    'SubjectPublicKeyInfo': 
                        {
                        'publicExponent': e,
                        'N': n
                        },
                    'PKCS10CertRequest': '-',
                    'Certificate': '-',
                    'PKCS7CertChain-PKCS': '-'
                    }
                }
                filename1 = str(input('Введите название файла для открытого ключа: '))
                with open(filename1, 'x', encoding = 'utf-8') as file1:
                    json.dump(OpenKey, file1, indent = 4)
                ClosedKey = {
                    'PrivateKey': {
                        'privateExponent': d,
                        'prime1': p,
                        'prime2': q,
                        'exponent1': exponent1,
                        'exponent2': exponent2,
                        'coefficient': coefficient
                    }
                }
                filename2 = str(input('Введите название файла для закрытого ключа: '))
                with open(filename2, 'x', encoding = 'utf-8') as file2:
                    json.dump(ClosedKey, file2, indent = 4)
                print('Файлы ключей сгенерированы')
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    work = False
            if choice == 2:
                pass
        else:
            print('\nСделайте правильный выбор!!!!!\n')





















    #m, a, b = extended_euclid(7919, 5)
    #print(f'НОД({7919}, {5}) = {m}')
    #print('Сгенерируйте параметры p и q:')
    #print('Параметр p')
    #p = simple_gen_k(int(input('')), int(input('')))
    #print('Параметр q')
    #q = simple_gen_k(int(input('')), int(input('')))

    #p = simple_gen_k(512, 10)
    #q = simple_gen_k(512, 10)
    #n = p * q
    #print(f'N = {n}')
    #x = (p-1)*(q-1)
    #print(x)
    #gen = True
    #while gen:
    #    e = int(input('Введите число e: '))
    #    m, a, b = extended_euclid(x, e)
    #    if m != 1:
    #        print('Выберите другое значение е')
    #        pass
    #    else:
    #        print('m:', m)
    #        gen = False
    #d = b
    #print(a, b, d)
#
    #string = 'hello world'
    #utf = string.encode('utf-8').hex()
    #print(int(utf, base = 16))
#
    #c = rsa_encryption(126207244316550804821666916, e, n)
    #print(rsa_encryption(126207244316550804821666916, e, n))
    #print(rsa_decryption(c, d, n))

    #simple_gen_k(88, 10)