import socket

host = 'localhost'
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port)) 
    server_socket.listen(1) 
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connection established with {client_address}")
            
            data = client_socket.recv(1024)
            
            if data:
                client_socket.sendall("Hello".encode())
                print(f"Message sent: {'Hello'}")
            else:
                print("No data received from client.")

