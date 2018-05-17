
#server side chat
import socket

serverSocket = socket.socket()#create new serverside socket
serverHostname = socket.gethostname()#get hostname of server
port = 12345 #set connection port
serverSocket.bind((serverHostname, port))#bind to port
serverSocket.listen(5)
client, address = serverSocket.accept()#establish connection with client
print("Connected to:", address)
#client.send("You have conneted to the server.")
while True:
        data = serverSocket.recv(1024)
        modifiedMessage, serverAddress = clientSocket.recvfrom(message.decode('utf-8'))
client.close()
