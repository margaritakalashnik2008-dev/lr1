import socket
import threading


HOST = "127.0.0.1"
PORT = 8080


def check_host(host):
    try:
        # Получаем IP-адрес указанного хоста
        ip = socket.gethostbyname(host)

        # Создаём TCP-сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Устанавливаем таймаут 3 секунды
        sock.settimeout(3)

        # Проверяем подключение к порту 80
        result = sock.connect_ex((ip, 80))

        sock.close()

        if result == 0:
            return "UP"
        else:
            return "DOWN"

    except Exception:
        return "DOWN"


def handle_client(client_socket, address):
    print(f"Підключено клієнта: {address}")

    try:
        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            request = data.decode().strip()
            print(f"Запит від {address}: {request}")

            parts = request.split()

            if len(parts) == 2 and parts[0] == "CHECK_HOST":
                host = parts[1]
                status = check_host(host)

                response = status
            else:
                response = "ERROR: невірний формат запиту"

            client_socket.sendall(response.encode())

    except Exception as e:
        print(f"Помилка: {e}")

    finally:
        client_socket.close()
        print(f"Клієнт відключений: {address}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen(5)

print(f"TCP-сервер запущено на {HOST}:{PORT}")
print("Очікування підключень...")


while True:
    client_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )

    thread.start()