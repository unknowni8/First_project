#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of input.')
    print('Syntax: python3 scanner.py <ip>')

print('.' * 50)
print("scaning target: " + target)
print("Time started: " + str(datetime.now()))
print('.' * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print('checking port {}'.format(port))
        if result == 0:
            print("port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
except socket.gaierror:
    print("Host name could not be resolved. ")
    sys.exit()
except socket.error:
    print("Couldn,t connect to server.")
    sys.exit()
