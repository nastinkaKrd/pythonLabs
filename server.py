import socket
import datetime
import time

# in commit 2 task 1.3 also
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1025
serverSocket.bind((host, port))
serverSocket.listen(1)
print(f"Сервер прослуховує на {host}:{port}")
clientSocket, clientAddress = serverSocket.accept()
print(f"З'єднано з {clientAddress}")
while True:
    dataFromClient = clientSocket.recv(1024)
    if not dataFromClient:
        break
    time.sleep(5)
    if dataFromClient.endswith(b'\n'):
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Отримано від клієнта повідомлення {dataFromClient.decode('utf-8')} ({currentTime})")

clientSocket.close()
serverSocket.close()
