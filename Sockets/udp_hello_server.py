import socket

host = "0.0.0.0"
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}...")

    while True:
            data, addr = server_socket.recvfrom(1024)
            print(f"Received data from {addr}: {data.decode()}")

            if data:
                response = f"Hello {data.decode()}"
                server_socket.sendto(response.encode(), addr)
            else:
                print("No data received.")

