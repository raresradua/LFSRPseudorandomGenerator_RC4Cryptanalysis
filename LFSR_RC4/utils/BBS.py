from utils.generator_utils import *


def create_bbs():
    bit_out = ""
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()
    n = p * q

    seed = current_time_to_seconds()
    x0 = (seed ** 2) % n
    for i in range(2 ** 10):
        bit_res = str(x0 % 2)
        x0 = (x0 ** 2) % n
        bit_out += bit_res
    print("======   BBS   ======")
    print("BBS OUTPUT: " + bit_out)
    bit_freq(bit_out)
