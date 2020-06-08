import socket
import random

 

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

 


 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):
    msgFromServer       = "12:32:07:452 225.912000 1.046000 0 0 0 0 2 0 0 0 592 598 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 241 241 1 1 1 0 39 37 39 38 39 37 0 0 2 2 0"

    bytesToSend         = str.encode(msgFromServer)

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)