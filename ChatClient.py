#Clientside chat
import socket

clientSocket = socket.socket() #create a new Clientside socket
clientHostname = socket.gethostname()#get hostname of machine
port = 12345 #set connection port

clientSocket.connect((clientHostname,port))
print(clientSocket.recv(1024))#print recived data from port 1024 where the server is
while True:
    message = input("->")#get message to send
    clientSocket.sendto(message.encode('utf-8'), (clientHostname, port))# encrypt message  and send
clientSocket.close # close when done
