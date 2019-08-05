import socket

def deviceName(d):
    x = socket.gethostbyaddr(str(d))
    return x

inp = ""
while inp == "": 
    inp = input("Enter the ip address: ")
    if inp:
        y = deviceName(inp)
        if y:
            print(y)
    else:
        print("IP Address is required!");
print("\n---------------------------------------\n");
print("The end!");