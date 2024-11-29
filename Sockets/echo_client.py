import socket

def main():
    message = input("Enter a message to send to the echo server: ")

    # Define server host and port
    host = 'localhost' 
    port = 5000  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Address Family: Internet, Socket Type: Stream
        s.connect((host, port))
        s.sendall(message.encode())
        
        response = s.recv(1024)
        
        print(f"Server response: {response.decode()}")

if __name__ == "__main__":
    main()
