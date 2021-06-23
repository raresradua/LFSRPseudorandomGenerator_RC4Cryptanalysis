import sympy
from datetime import datetime
import random


def current_time_to_seconds():
    current_time = datetime.now().time()
    in_seconds = current_time.second + current_time.minute * 60 + current_time.hour * 3600
    return in_seconds


def generate_large_prime():
    current_prime = sympy.randprime(2 ** 511, 2 ** 1024)
    return current_prime


def bit_freq(bit_out):
    freq = {}
    for i in range(len(bit_out)):
        if bit_out[i] in freq:
            freq[bit_out[i]] += 1
        else:
            freq[bit_out[i]] = 1
    for i in freq:
        print(i + ": " + str((freq[i] * 100 / len(bit_out))) + "%")