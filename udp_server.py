import socket

HOST = "127.0.0.1"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print(f"UDP-сервер запущено на {HOST}:{PORT}")
print("Очікування UDP-повідомлень...")


while True:
    data, address = server.recvfrom(1024)

    message = data.decode()

    print(f"Отримано від {address}: {message}")

    # Імітація втрати пакетів:
    # сервер не відповідає на PING 3 та PING 5
    if message in ["PING 3", "PING 5"]:
        print("Пакет пропущено — відповідь не надсилається")
        continue

    response = "PONG"

    server.sendto(response.encode(), address)