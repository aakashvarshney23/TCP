def calculate_in(number):
    updated = [i for i in number.split(",")]
    flag = True
    for items in updated:
        if not items.isdigit():
            if items.startswith("-"):
                if not items[1:].isdigit():
                    flag = False
            else:
                flag = False

    if flag == False:
        return "Invalid"

    updated = [int(i) for i in updated]
    new_list = updated[1:]
    if updated[0] != len(new_list):
        return "Invalid Length"
    result = (
    "Max: ", max(new_list), "Min: ", min(new_list), "Mean: ", float(sum(new_list) / len(new_list)),
    "Total: ",
    sum(new_list))
    result = str(result)
    return result

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")


while True:
    connectionSocket, addr = serverSocket.accept()
    get_input = connectionSocket.recv(1024).decode()
    get_ouput = calculate_in(get_input)
    connectionSocket.send(get_ouput.encode())
    connectionSocket.close()
