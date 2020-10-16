import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#here we use socket.gethostname() because it is localmachine, but usually you will us an ip address
s.connect((socket.gethostname(), 1234)) 

while True:

    full_msg = ''
    new_msg = True

    #getting a tcp byte stream of data, we have to decide how many chunks of data we want to receive at the same time, 
  #1024 is enough for us but this gets complicated
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        
        #must decode the byte stream of data
        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            print("Full Message Received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
        
    print(full_msg)