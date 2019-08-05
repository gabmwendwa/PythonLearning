# Echo client program
import socket

# HOST = 'daring.cwi.nl'    # The remote host
# HOST = '127.0.0.1'    # The remote host
HOST = '192.168.1.50'    # The remote host
PORT = 3002              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, server')
    data = s.recv(1024)
print('Received', repr(data))