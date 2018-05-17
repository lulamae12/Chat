
#server side chat
import socket
serverSocket = socket.socket()#create new serverside socket
serverHostname = socket.gethostname()#get hostname of server
port = 12345 #set connection port
serverSocket.bind((serverHostname, port))#bind to port
ConnectionMessage = ("You have connected to:" + serverHostname)
serverSocket.listen(5)
client, address = serverSocket.accept()#establish connection with client
print("Connected to:", address)
message = ConnectionMessage
client.sendto(message.encode(),(serverHostname, port))
while True:
        data = client.recv(1024)
        #modifiedMessage, serverAddress = serverSocket.recvfrom(message.decode('utf-8'))
        print('Received message:', client.recv(1024))
client.close()
