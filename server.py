import socket
import datetime
import time
import threading

host = "127.0.0.1"
port = 1027


def handle_client(client_socket, client_address):
    print(f"З'єднано з {client_address}")
    try:
        while True:
            data_from_client = client_socket.recv(1024)
            time.sleep(5)
            if len(data_from_client) > 0:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Отримано від клієнта повідомлення {data_from_client.decode('utf-8')} ({current_time})")
                clientSocket.sendall(data_from_client)
    except ConnectionResetError:
        pass
    finally:
        print(f"Закрито з'єднання з {clientAddress}")
        clientSocket.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((host, port))
    serverSocket.listen(2)
    while True:
        clientSocket, clientAddress = serverSocket.accept()
        t = threading.Thread(target=handle_client, args=(clientSocket, clientAddress))
        t.start()
