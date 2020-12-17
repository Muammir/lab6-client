import socket
import sys

ClientSocket = socket.socket()
host = '192.168.1.9'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input = input('\nPlease choice your mathematic operation\n(Log):Logarithm\n(Square):Square root\n(Exp):Exponential\n(Quit):Exit\nAnswer :')
##    Input = input('Say Something: ')
    if Input == 'Log' or Input == 'Square' or Input == 'Exp':
        value = input("Enter a number: ")
        Input = Input + ":" + value
        ClientSocket.send(str.encode(Input))
    elif Input == 'Quit':
        print("Exit...")
        ClientSocket.send(str.encode(Input))
        sys.exit()
    else:
        print("Invalid")
        sys.exit()

    Response = ClientSocket.recv(1024)
    print("Answer after math operation :")
    print(Response.decode('utf-8'))

ClientSocket.close()
