from utils.generator_utils import *


def generate_a(n):
    return random.randint(1, n)


def gcd(a, n):
    while n != 0:
        a, n = n, a % n
    return a


def coprime(a, n):
    return gcd(a, n) == 1


def jacobi(a, n):
    b = a % n
    c = n
    s = 1
    while b >= 2:
        while b % 4 == 0:
            b = b // 4
        if b % 2 == 0:
            if c % 8 == 3 or c % 8 == 5:
                s = -s
            b = b // 2
        if b == 1:
            break
        if b % 4 == c % 4 == 3:
            s = -s
        b, c = c % b, b
    return s * b


def create_jacobi():
    bit_out = ""
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()
    n = p * q
    a = generate_a(n)
    while not coprime(a, n):
        a = generate_a(n)
    for i in range(2 ** 10):
        jacobi_symbol = jacobi(a + i + 1, n)
        bit_res = int((jacobi_symbol + 1) / 2)
        bit_out += str(bit_res)
    print("======   Jacobi   ======")
    print("Jacobi OUTPUT: " + bit_out)
    bit_freq(bit_out)
