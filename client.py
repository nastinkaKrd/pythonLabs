import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1025
client_socket.connect((host, port))
message = input("Введіть текст для сервера >> ")
client_socket.send(message.encode('utf-8'))
response = client_socket.recv(1024)
print(f"Відповідь від сервера: {response.decode('utf-8')}")

client_socket.close()
