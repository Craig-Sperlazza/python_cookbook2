# https://linuxhint.com/python-for-hacking-port-scanner/

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Enter Target IP')

def scanner(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False
for portNumber in range(1, 1236):
    print(f"Scanning port: {portNumber}")
    if scanner(portNumber):
        print(f"[*] Port {portNumber} /tcp is open")