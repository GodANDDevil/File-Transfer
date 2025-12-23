import socket
import RSA


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, port))
    while True:
        public, private = RSA.rsa()
        filename = input("Enter the file name:")
        fi = open(filename, 'r')
        data = fi.read()
        if not data:
            break

        while data:
            ed = str(input("Do you want Encryption(1) or Decryption(2):"))
            if ed == '1':
                data = RSA.encryption(data, public)
                sock.send(data.encode())
                data = fi.read()
            elif ed == '2':
                data = RSA.decryption(data, private)
                sock.send(data.encode())
                data = fi.read()
            else:
                break
        fi.close()
    fi.close()
