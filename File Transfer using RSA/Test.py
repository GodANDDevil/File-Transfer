import RSA

a = "hi"
pub, pri = RSA.rsa()
print("Public Key:", pub)
print("Private Key:", pri)

enc = RSA.encryption(a, pub)
print("Encrypted:", enc)

dec = RSA.decryption(enc, pri)
print("Decrypted:", dec)
