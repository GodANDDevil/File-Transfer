import math
import random

def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    a = 5
    while a * a <= x:
        if x % a == 0 or x % (a + 2) == 0:
            return False
        a += 6
    return True


def make_prime(x):
    if is_prime(x):
        return x
    else:
        return make_prime(x+1)


def co_prime(x):
    if x <= 1:
        return 2
    for n in range(2, x+1):
        if math.gcd(x, n) == 1:
            return n
    return x + 1


def value_finder(e, n2, x=1):
    while (e*x) % n2 != 1:
        x = x+1
    return x


def encryption(m, public_key):
    encrypted_data = ""
    for x in m:
        if x == " ":
            encrypted_data += " "
        else:
            x1 = convert_str_to_int(x)
            data = (pow(x1,public_key[0],public_key[1]))%25
            data = convert_int_to_str(data)
            x1 = str(data)
            # x1 = convert_int_to_str(data % 26)
            encrypted_data += x1+','
    return encrypted_data

#     e, n = public_key
#     encrypted_numbers = []
#     for ch in m:
#         if ch == " ":
#             encrypted_numbers.append(" ")  # marker for space
#         else:
#             m = ord(ch) % n
#             c = pow(m, e, n)
#             encrypted_numbers.append(str(c))
#     return ",".join(encrypted_numbers)

# def encryption(message, public_key):
#     e, n = public_key
#     ciphertext = [pow(ord(ch) % n, e, n) for ch in message]
#     return ciphertext

def convert_str_to_int(x):
    return ord(x) - ord('a')


def convert_int_to_str(x):
    return chr(x + ord('a'))


def file_encryption():
    pass


def decryption(c, private_key):
    decrypted_data = ""
    for x in c:
        if x == " ":
            decrypted_data += " "
        elif x == ",":
            continue
        else:
            x1 = convert_str_to_int(x)
            data = (pow(x1, private_key[0], private_key[1]))
            x1 = convert_int_to_str(data % 25)
            decrypted_data += x1
    return decrypted_data
#
#     d, n = private_key
#     decrypted_data = ""
#     for token in c.split(","):
#         if token == "":
#             continue
#         elif token == " ":
#             decrypted_data += " "
#         else:
#             c = int(token)
#             m = pow(c, d, n)
#             decrypted_data += chr(m)
#     return decrypted_data

# def decryption(ciphertext, private_key):
#     d, n = private_key
#     plaintext_chars = [chr(pow(c, d, n)) for c in ciphertext]
#     return "".join(plaintext_chars)

def file_decryption():
    pass


def rsa():
    x = 5
    if is_prime(x):
        pass
    else:
        x = make_prime(x)
    print(f"x:{x}")

    y = 11
    if is_prime(y):
        pass
    else:
        y = make_prime(x)
    print(f"y:{y}")

    if x == y:
        y += 1
    y = make_prime(y)

    n1 = x * y
    n2 = (x - 1) * (y - 1)
    # print(f"x:{x}")
    # print(f"y:{y}")

    e = co_prime(n2)
    print(e)
    d = value_finder(e, n2)
    print(d)

    public_key = [e, n1]
    private_key = [d, n1]

    return public_key, private_key


