import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1027
client_socket.connect((host, port))
while True:
    message = input("Введіть текст для сервера (або 'exit' для виходу): ")
    if message == 'exit':
        break
    client_socket.send(message.encode('utf-8'))

client_socket.close()
