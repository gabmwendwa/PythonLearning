import socket
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

from subprocess import Popen, PIPE, STDOUT

try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    host = str(host)

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    v = subprocess.call(command, stdin=PIPE, stdout=DEVNULL, stderr=STDOUT) == 0
    if v:
        print("------------------------")
        print("Device is online")
        print("------------------------")
        if deviceName(host):
            print("------------------------")
            print("Do something else!")
            print("------------------------")
    else:
        print("------------------------")
        print("Sorry! Device not online")
        print("------------------------")

def deviceName(d):
    x = socket.gethostbyaddr(str(d))
    if x:
        print("------------------------")
        print(x)
        print("------------------------")
        return True
    else:
        print("------------------------")
        print("Sorry! Cannot get device name")
        print("------------------------")
        return False

inp = ""
while inp == "": 
    inp = input("Enter the ip address/host name: ")
    if inp:
        ping(inp)
    else:
        print("Input is required!");

print("------------------------")
print("THIS IS THE END")
print("------------------------")
