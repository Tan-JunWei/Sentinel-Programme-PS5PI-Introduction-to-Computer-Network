import socket

message = input("Enter the name of a city: ")

host = 'localhost' 
port = 5000  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(message.encode())
    
    response = s.recv(1024)
    
    print(f"{response.decode()}")

