# https://www.youtube.com/watch?v=Lbfe3-v7yE0

import socket
import time

#we are going to create a header that is sent to the client which tells them the size, 
# so the client can wait until it receives that full size
#going to create a fixed length header so noone can mess with it
# msg = "Welcome to the server!"
# print(f'{len(msg):<10}'+msg)
# will print: 22........ "Welcome to the server!"
#note 10 is 1,000,000,000 characters
HEADERSIZE = 10

#create the socket object
#AF_INET is IPv4 , SOCK_STREAM is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to a tuple
#(ip:localhost, port)
s.bind((socket.gethostname(), 1234))

#must make the server listen
#this server will listen to a queue of 5
s.listen(5)

#listen forever
#we will listen forever for connections 
# it will create a client socket object stored in clientsocket
# s.accept() will contain their ip address and we store it in address
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    msg = "Welcome to the server!"
    #< makes it left aligned
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    #we send info to our clientsocket
    clientsocket.send(bytes(msg, "utf-8"))
    
    #to show the connection stays open we wills end a message every 3 seconds
    while True:
        time.sleep(3)
        msg = f'The time is: {time.time()}'
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))