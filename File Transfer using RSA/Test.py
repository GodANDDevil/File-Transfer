import RSA

a = "hi"
pub, pri = RSA.rsa()
print("Public Key:", pub)
print("Private Key:", pri)

enc = RSA.encryption(a, pub)
print("Encrypted:", enc)

dec = RSA.decryption(enc, pri)
print("Decrypted:", dec)

def decryption(c):
    decrypted_data = ""
    for x in c:
        if x == " ":
            decrypted_data += " "
        elif x == ",":
            continue
        else:
            x1 = RSA.convert_str_to_int(x)
            data = (pow(x1, 43, 77))+1
            x1 = RSA.convert_int_to_str(data % 25)
            decrypted_data += x1
    return decrypted_data
a = decryption('b')
print(a)