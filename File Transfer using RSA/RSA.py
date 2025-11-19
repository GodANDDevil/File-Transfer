import math


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
            data = (pow(x1,public_key[0], public_key[1]))
            x1 = convert_int_to_str(data % 26)
            encrypted_data += x1
    return encrypted_data

    # encrypted_data = []
    # for x in m:
    #     if x == " ":
    #         encrypted_data.append(" ")
    #     else:
    #         x1 = convert_str_to_int(x)
    #         data = pow(x1, public_key[0], public_key[1])
    #         encrypted_data.append(str(data))  # store full encrypted int
    # return " ".join(encrypted_data)


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
        else:
            x1 = convert_str_to_int(x)
            data = (pow(x1, private_key[0], private_key[1]))
            x1 = convert_int_to_str(data % 26)
            decrypted_data += x1
    return decrypted_data

    # decrypted_data = []
    # for x in c:
    #     if x == " ":
    #         decrypted_data += " "
    #     else:
    #         x1 = int(x)
    #         data = pow(x1, private_key[0], private_key[1])
    #         decrypted_data.append(str(data))
    # return decrypted_data


def file_decryption():
    pass


def rsa():
    x = int(input("Enter First number:"))
    if is_prime(x):
        pass
    else:
        x = make_prime(x)
    print(f"x:{x}")

    y = int(input("Enter Second number:"))
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
    d = value_finder(e, n2)

    public_key = [e, n1]
    private_key = [d, n1]

    return public_key, private_key


