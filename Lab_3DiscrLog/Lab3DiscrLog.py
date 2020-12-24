import math


def eulers_phi(p):
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
    print(r)
    return r 


def divisors_of_a_number(r):
    divisors = [x for x in range (1, r // 2 + 1) if r % x == 0] + [r]          
    print (divisors)
    return divisors


def order_of_a(a, p, divisors):
    vip_ner = list()
    for d in divisors:
        a1 = a ** d % p
        if a1 % p == 1:
            vip_ner.append(d)
        else:
            continue
    print(vip_ner)
    order = min(vip_ner)
    print(order)
    return order
    





if __name__ == "__main__":
    p = 401
    r = eulers_phi(p)
    div = divisors_of_a_number(r)
    order_of_a(10, p, div)
    


