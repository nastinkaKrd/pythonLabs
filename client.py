import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1025
clientSocket.connect((host, port))
while True:
    message = input("Введіть текст для сервера (або 'exit' для виходу): ")
    if message == 'exit':
        break
    message += '\n'
    clientSocket.send(message.encode('utf-8'))

clientSocket.close()
