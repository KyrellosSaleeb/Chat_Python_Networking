from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))


print ('The server is ready to receive')
serverSocket.listen(1)
print(f"listening at {serverSocket.getsockname()}")
connectionSocket, addr = serverSocket.accept()
print(f"server is now connected to {connectionSocket.getsockname()}")
print(f"Socket connects between {serverSocket.getsockname()} and {addr}")

print ('The server is ready to receive')

while True:
     
     sentence = connectionSocket.recv(1024).decode()
     if sentence != "Exit":
            print(f"Recieved message from client: {sentence}")
            #capitalizedSentence = sentence.upper()
            #connectionSocket.send(capitalizedSentence.encode())
            serverMessage=f"Your data was {len(sentence)} bytes"
            connectionSocket.send(serverMessage.encode())
     else:
            serverMessage=f"Disconnect"
            connectionSocket.send(serverMessage.encode())
            print("Reply sent, Server socket closed")
            break

connectionSocket.close()
     
