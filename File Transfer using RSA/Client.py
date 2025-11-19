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
            # data = RSA.encryption(data, public)
            # sock.send(data.encode())
            # data = fi.read()
            data = RSA.decryption(data, private)
            sock.send(data.encode())
            data = fi.read()
        fi.close()
    fi.close()
