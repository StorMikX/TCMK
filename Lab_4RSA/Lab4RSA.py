import random
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


def rsa_encryption(m, e, n):
    c = pow(m, e, n)
    return int(c)


def rsa_decryption(c, d, n):
    m = pow(c, d, n)
    return int(m)


def tohex(n):
    alpha = '0123456789abcdef'
    out = '' if n else '0'
    while n > 0:
        out = alpha[n % 16] + out
        n >>= 4
    return out


def decode_unicode(n):
    text = bytes.fromhex(n).decode('utf-8')
    return text


if __name__ == "__main__":
    work = True
    while work:
        print('\n\t---RSA Menu---\n'
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
                        'coefficient': coefficient,
                        'N': n
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
                e = pkdata['PublicKey']['SubjectPublicKeyInfo']['publicExponent']
                n = pkdata['PublicKey']['SubjectPublicKeyInfo']['N']
                m = m.encode('utf-8').hex()
                m = int(m, base = 16)
                encrypt = rsa_encryption(m, e, n)
                encryptedtext = tohex(encrypt)
                encmes = {
                    'EncryptedMessage': 
                    {
                        'Version': 0,
                        'EncryptedContentInfo':
                        {
                            'ContentType': 'text',
                            'ContentEncryptionAlgorithmIdentifier': 'rsaEncryption',
                            'encryptedContent': encryptedtext,
                            'OPTIONAL': '-'

                        }
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
                c = encryptdat['EncryptedMessage']['EncryptedContentInfo']['encryptedContent']
                privatekeyfile = str(input('Введите название файла с закрытым ключом(json): '))
                if privatekeyfile.endswith('.json'):
                    with open(privatekeyfile, 'r') as pvfile:
                        pvdata = json.load(pvfile)
                else:
                    print('Неправильнй формат файла с открытым ключом!!!')
                    break
                d = pvdata['PrivateKey']['privateExponent']
                n = pvdata['PrivateKey']['N']
                mes = int(c, base = 16)
                decrypt = rsa_decryption(mes, d, n)
                texthex = tohex(decrypt)
                decryptxt = decode_unicode(texthex)
                filename4 = input('Введите название файла с расшифрованным текстом: ')
                with open(filename4, 'w') as decr:
                    decr.write(decryptxt)
                print('Сообщение успешно расшифровано и записано в отдельный документ')
                next = input("Продолжить работу? Y/N\n ").lower()
                if next=="y":
                    pass
                else:
                    work = False
            if choice == 4:
                work = False
        else:
            print('\nСделайте правильный выбор!!!!!\n')    