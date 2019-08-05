# Echo client program
import socket
import sys

# HOST = 'daring.cwi.nl'    # The remote host
# HOST = '127.0.0.1'    # The host
# PORT = 50007              # The same port as used by the server

HOST = '192.168.1.50'    # The remote host
PORT = 3002              # The same port as used by the server

s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    # s.2(b'Hello, world')
    # data = s.recv(1024)
# print('Received', repr(data))
	dataold = 'begin'
	while True:
		data = s.recv(1024)
		if data:
			# print('Received', repr(data))
			if data != dataold:
				print(data)
				data = dataold;
		else:
			break