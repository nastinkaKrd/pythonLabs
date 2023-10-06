import socket
import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1025
serverSocket.bind((host, port))
serverSocket.listen(1)
print(f"Сервер прослуховує на {host}:{port}")
clientSocket, clientAddress = serverSocket.accept()
print(f"З'єднано з {clientAddress}")
dataFromClient = clientSocket.recv(1024)
if dataFromClient:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Отримано від клієнта повідомлення {dataFromClient.decode('utf-8')} ({current_time})")
response = "Повідомлення отримано!"
clientSocket.send(response.encode('utf-8'))

clientSocket.close()
serverSocket.close()
