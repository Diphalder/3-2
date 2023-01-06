import socket 

HOST='127.0.0.1' # server address

PORT=9999 # which port of the server what to communicate

socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# send rqst and get ack 


socket.connect((HOST,PORT))

while 1:
    message=input("Enter your Message = ")
    socket.send(message.encode('utf-8'))   # formating
    if(message=="exit"):
        print(socket.recv(1024).decode('utf-8'))
        break
    print("msg from server = "+socket.recv(1024).decode('utf-8')) 
 



