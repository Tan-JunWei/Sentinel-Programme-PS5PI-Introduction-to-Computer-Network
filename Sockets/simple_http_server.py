import socket

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode() 

    # Get the requested path from the request
    request_line = request_data.splitlines()[0]
    requested_path = request_line.split(" ")[1]

    if requested_path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n" 
        response += "<html><body><h1>Welcome to my simple HTTP server!</h1></body></html>"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n" 
        response += "<html><body><h1>404 Not Found</h1></body></html>"

    client_socket.send(response.encode()) 
    client_socket.close()

def start_server():
    server_socket = socket.socket() 
    server_socket.bind(("localhost", 8000)) 
    server_socket.listen()
    print("Server is running on http://localhost:8000")

    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}") 
        handle_request(client_socket)

start_server()
