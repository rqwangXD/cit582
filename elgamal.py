import random

from params import p
from params import g

def keygen():
    a = random.randint(1, p)
    sk = a
    h = pow(g, a, p)
    pk = h
    return pk,sk

def encrypt(pk,m):
    q = (p - 1) / 2
    r = random.randint(1, q)
    c1 = pow(g, r, p)
    print('c1: ', c1)
    c2 = (pow(pk, r, p) * (m % p)) % p
    print('c2: ', c2)
    return [c1,c2]

def decrypt(sk,c):
    m = ((c[1] % p) * pow(c[0], -1 * sk, p)) % p
    return m


