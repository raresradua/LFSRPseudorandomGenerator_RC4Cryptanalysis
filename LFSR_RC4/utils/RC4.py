from random import randint


def create_rc4_generator(key):
    def initial_state(key):
        j = 0
        key_length = len(key)
        s = []
        for i in range(256):
            s.append(i)

        for i in range(256):
            j = (j + s[i] + key[i % key_length]) % 256
            s[i], s[j] = s[j], s[i]

        return 0, 0, s

    def transition(i, j, s):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]

        byte = s[(s[i] + s[j]) % 256]
        return i, j, s, byte

    def rc4gen():
        i, j, s0 = initial_state(key)
        while True:
            i, j, s0, byte = transition(i, j, s0)
            yield byte

    return rc4gen


def generate_key():
    key_length = 16  # 5 <= key_length <= 16
    key = []
    for i in range(key_length):
        element = randint(0, 255)
        key.append(element)
    return key
