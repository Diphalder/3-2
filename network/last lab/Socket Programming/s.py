import socket 

HOST='127.0.0.1'
# HOST='127.0.0.1' when no internet connection LOCAL host
PORT= 9999

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# af -> address family internet type
#2 type of stream 
# #for UDP socket_stream

server.bind((HOST,PORT))

# ready for communication

server.listen(5)

# ON for client .. client can send rqst
#queue lenth is 5



while True:  # give client unlimited time
    communication_socket,address = server.accept()   #    , client site ip address
    print(f"Connected to {address}") 
    while 1:
        message = communication_socket.recv(1024).decode('utf-8')      # at e time 1024byte can recive
        if(message=="exit"):
            communication_socket.send(f" Server exit your connection ".encode('utf-8'))
            communication_socket.close()
            print(f"Connection with {address} ended")
            break
        print(f"Message from Client is: {message}")
        msg=input("Enter your Message = ") 
        communication_socket.send(msg.encode('utf-8')) 
    







