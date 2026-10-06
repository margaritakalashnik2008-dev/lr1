import socket

HOST = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Підключено до TCP-сервера.")

while True:
    request = input("Введіть запит: ")

    if request.lower() == "exit":
        break

    client.sendall(request.encode())

    response = client.recv(1024).decode()

    print("Відповідь сервера:", response)

client.close()