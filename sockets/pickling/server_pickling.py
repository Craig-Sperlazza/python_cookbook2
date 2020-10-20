# https://www.youtube.com/watch?v=WM1z8soch0Q
# pickling---taking a python object, serializing it into bytes, 
# sending it, then taking it and converting it back to python object
# we are going to pickle a dictionary but you would liekly use json for this

import socket
import time
import pickle


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

    d = {1: "Hey", 2: "There"}
    #turn it into string data
    msg = pickle.dumps(d)

    #message is bytes, now we have to convert header to bytes too
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    #we send info to our clientsocket
    clientsocket.send(msg)
    
