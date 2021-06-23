import time

from utils.BBS import *
from utils.Jacobi import *
from utils.LFSR import *
from utils.RC4 import *


def main():
    start_time = time.time()
    create_bbs()
    print("======    BBS Execution Time: %s seconds   ======\n\n\n" % (time.time() - start_time))

    start_time = time.time()
    create_jacobi()
    print("======    Jacobi Execution Time: %s seconds   ======\n\n\n" % (time.time() - start_time))

    start_time = time.time()
    lfsr = create_lfsrgenerator((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1), 8)()
    values_lfsr = [i for i in lfsr]
    string_values_lfsr = ''.join(str(element) for element in values_lfsr)
    print("======    LFSR OUTPUT:\n" + string_values_lfsr)
    print("======    LFSR Execution Time: %s seconds   ======\n\n\n " % (time.time() - start_time))

    start_time = time.time()
    print("======    RC4 OUTPUT:")
    number_of_zeros = 0
    for i in range(2 ** 16):
        key = generate_key()
        rc4 = create_rc4_generator(key)()
        for j in range(256):
            byte = next(rc4)
            if j == 1:
                if byte == 0:
                    number_of_zeros += 1
    p = float(number_of_zeros) / 2 ** 16
    expected = float(1.0 / 128)

    print("Number of zeros/iteration number: " + str(p) + "\n" + "Expected ratio of zeros(1/128): " + str(expected))
    if p > expected:
        print("Bias observed!")
    else:
        print("Bias missed!")
    print("======    RC4 Execution Time: %s seconds   ======" % (time.time() - start_time))


if __name__ == '__main__':
    main()
