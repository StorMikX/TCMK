import random
import json


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
    y = (pow(a, r, n)) 
    if y != 1 and y != n-1:
        j = 1
        if j <= s - 1 and y != n-1:
            y = (y * y) % n
            if y == 1:
                return 0
            j = j + 1
        if y != n - 1:
            return 0
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
            return p


def divisors_of_a_number(r):
    divisors = []
    divisors.append(r)
    return divisors


def order_of_a(a, p, divisors):
    #Вычисление порядка числа а
    vip_ner = list()
    for d in divisors:
        a1 = pow(a, d, p)
        if a1 % p == 1:
            vip_ner.append(d)
        else:
            continue
    order = min(vip_ner)
    return order


def el_gamal_encryption(m, alpha, beta, p):
    r = random.randint(1, p - 2)
    c1 = int(pow(alpha, r, p))
    c2 = (m * pow(beta, r)) % p
    return c1, c2


def tohex(n):
    alpha = '0123456789abcdef'
    out = '' if n else '0'
    while n > 0:
        out = alpha[n % 16] + out
        n >>= 4
    return out

    
if __name__ == "__main__":
    work = True
    while work:
        print('\n\t---ElGamal Menu---\n'
              '1) Генерация параматров ключей\n'
              '2) Шифрование\n'
              '3) Расшифрование\n'
              '4) Выход из программы шифрования')
        choice = (int(input('Выберите функцию программы: ')))
        if choice >= 1 and choice < 5:
            if choice == 1:
                print('\nГенерация параметра p')
                k1 = int(input('Укажите двоичную разрядность числа p: '))
                t1 = int(input('Укажите число итераций генератора числа p: '))
                p = simple_gen_k(k1, t1)
                print(f'p = {p}')
                a = random.randint(1, p - 2)
                while True:
                    alpha = random.randint(1, p - 1)
                    er = p - 1
                    div = divisors_of_a_number(er)
                    order = order_of_a(alpha, p, div)
                    if order != p - 1:
                        continue
                    else: 
                        break
                beta = pow(alpha, a, p)
                OpenKey = {
                    'PublicKey': 
                    {
                        'p': p,
                        'alpha': alpha,
                        'beta': beta
                    }
                }
                filename1 = str(input('Введите название файла для открытого ключа: '))
                with open(filename1, 'x', encoding = 'utf-8') as file1:
                    json.dump(OpenKey, file1, indent = 4)
                PrivateKey = {
                    'PrivateKey':{
                        'a': a,
                        'p': p
                    }
                }
                filename2 = str(input('Введите название файла для закрытого ключа: '))
                with open(filename2, 'x', encoding = 'utf-8') as file2:
                    json.dump(PrivateKey, file2, indent = 4)
                print('Файлы ключей сгенерированы')
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    work = False
            if choice == 2:
                namefile1 = input('Введите название файла для шифрования(txt): ')
                if namefile1.endswith('.txt'):
                    with open(namefile1 , 'r') as textfile:
                        m = textfile.read()
                else:
                    print('Неправильный формат файла!!!')
                    break
                publickeyfile = str(input('Введите название файла с открытым ключом(json): '))
                if publickeyfile.endswith('.json'):
                    with open(publickeyfile, 'r') as pkfile:
                        pkdata = json.load(pkfile)
                else:
                    print('Неправильнй формат файла с открытым ключом!!!')
                    break
                alpha = pkdata['PublicKey']['alpha']
                beta = pkdata['PublicKey']['beta']
                p = pkdata['PublicKey']['p']
                m = m.encode('utf-8').hex()
                m = int(m, base = 16)
                encrypt1, encrypt2 = el_gamal_encryption(m, alpha, beta, p)
                encryptedtxt1 = tohex(encrypt1)
                encryptedtxt2 = tohex(encrypt2)
                encmes = {
                    'EncryptedMessage': {
                        'encryptedContent1': encryptedtxt1,
                        'encryptedContent2': encryptedtxt2
                    }
                }
                filename3 = str(input('Укажите название файла с зашифрованным сообщением: '))
                with open(filename3, 'x', encoding = 'utf-8') as file3:
                    json.dump(encmes, file3, indent = 4)
                print('Сообщение зашифровано и помещено в специальный файл')
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    work = False
            if choice == 3:
                namefile2 = input('Введите название файла для расшифрования(json): ')
                if namefile2.endswith('.json'):
                    with open(namefile2 , 'r') as textfile1:
                        encryptdat = json.load(textfile1)   
                else:
                    print('Неправильный формат файла!!!')
                    break
                c1 = encryptdat['EncryptedMessage']['encryptedContent1']
                c2 = encryptdat['EncryptedMessage']['encryptedContent2']

        

                