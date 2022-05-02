from socket import *
serverIP = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))

while True:
    sentence = input('Input lowercase sentence or type Exit to disconnect: ')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)

    print ('From Server:', modifiedSentence.decode())

    if modifiedSentence.decode()=="Disconnect":
            print("Your are now disconnected from the server")
            break

exit(1)
clientSocket.close()
