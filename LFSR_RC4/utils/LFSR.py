import math


def create_lfsrgenerator(taps, seed):
    def lfsrgen():
        degree = len(taps)  # gradul polinomului de feedback
        period = math.pow(2, degree)  # perioada
        value = seed  # valoarea initiala
        iteration = 0
        while iteration < period:
            bit = 0

            for j in range(degree):
                if taps[j]:
                    bit ^= value >> j
            bit &= 1
            value = (value >> 1) | (bit << (degree - 1))  # scapam de cel mai putin semnificativ bit si il punem pe cel nou gasit
            iteration += 1
            yield bit

    return lfsrgen
