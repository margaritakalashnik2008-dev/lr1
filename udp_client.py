import socket

HOST = "127.0.0.1"
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.settimeout(2)

for i in range(5):
    message = f"PING {i + 1}"

    client.sendto(message.encode(), (HOST, PORT))

    try:
        data, address = client.recvfrom(1024)

        print(f"{message} -> {data.decode()}")

    except socket.timeout:
        print(f"{message} -> TIMEOUT")

client.close()