numbers = input(" Enter the length and then the numbers separated by a comma : ")

from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(numbers.encode())
get_output = clientSocket.recv(1024)
print('From Server: ', get_output.decode())
clientSocket.close()