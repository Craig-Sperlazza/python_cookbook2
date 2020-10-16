# https://www.youtube.com/watch?v=Lbfe3-v7yE0

import socket
import time

#we are going to create a header that is sent to the client which tells them the size, so the client can wait until it receives that fuill size
#going to create a fixed length header so noone can mess with it
# msg = "Welcome to the server!"
# print(f'{len(msg):<10}'+msg)
HEADERSIZE = 10


#AF_INET is IPv4 , SOCK_STREAM is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#localhost, port
s.bind((socket.gethostname(), 1234))

#server will listen to a queue of 5
s.listen(5)

#we will listen forever for connections and we will create a client socket object stored in s.accept() with their address
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    msg = "Welcome to the server!"
    #< makes it left aligned
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))
    
    #to show the connection stays open we wills end a message every 3 seconds
    while True:
        time.sleep(3)
        msg = f'The time is: {time.time()}'
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))