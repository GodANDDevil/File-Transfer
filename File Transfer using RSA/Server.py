import socket
import RSA
import json

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    number_clients = int(input("Enter the nuber of Clients:"))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(number_clients)
    connection = []
    print("Initiating clients")

    for i in range(number_clients):
        conn = sock.accept()
        connection.append(conn)
        print("Connected with Client ",i+1)

    fileno = 1
    idx = 0
    for conn in connection:
        idx += 1
        data = conn[0].recv(1024).decode()
        if not data:
            continue
        filename = 'File'+str(fileno)+'.txt'
        fileno = fileno +1
        fo = open(filename,'w')
        while data:
            if not data:
                break
            else:
                fo.write(data)
                data = conn[0].recv(1024).decode()
        print()
        print("Receiving file from client ",idx)
        print()
        print("Received Succesfully! New filename is: ",filename)
        fo.close()

    #clossing connection
    for conn in connection:
        conn[0].close()
