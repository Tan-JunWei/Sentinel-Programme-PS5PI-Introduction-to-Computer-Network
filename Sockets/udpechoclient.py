import socket

def send_message():
    message = input("Enter a message to send to the echo server: ")

    # Define server host and port
    host = 'localhost' 
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # s.connect((host, port))
        s.sendto(message.encode(), (host, port))
        
        data, addr = s.recvfrom(1024)
        print(f"Received response from server: {data.decode()}")

send_message()
