import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#how to close the port so we can reuse address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}

print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header): #basically the client did not send any data
            return False
        
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    
    except:
        return False

while True:
    #honeslty all we care about at this point is the read_sockets, should later figure out exceptiuon sockets
    read_sockets, _, exception_sockets = select.select(sockets_list, [], [])

    for notified_sockets in read_sockets:
        #first condition is if someone just connects
        if notified_socket == server_socket:
            # The return value of server_socket.accept() is a pair (conn, address) 
            # where conn is a new socket object usable to send and receive data on the connection, 
            # and address is the address bound to the socket on the other end of the connection.
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)    
            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}: {client_address[1]} username: {user['data'].decode('utf-8')}")

        else:
            #for someone already connected
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed Connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Received Message From {user['data'].decode('utf-8')} and the message is: {message['data'].decode('utf-8')}")

            #share the message with everybody but sender
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
            
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket] 










