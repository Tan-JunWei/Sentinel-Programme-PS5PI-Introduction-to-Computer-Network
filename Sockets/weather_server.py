import socket 

weather_data = {
"London": {"temperature": 18, "humidity": 60, "description": "Partly cloudy"},
"Paris": {"temperature": 22, "humidity":
55, "description": "Sunny"},
"New  York":  {"temperature":  20, "humidity": 70, "description": "Cloudy"},
"Tokyo": {"temperature": 25, "humidity": 80, "description": "Rainy"}
}

host = 'localhost'
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port)) 
    server_socket.listen(1) 
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            
            data = client_socket.recv(1024)
            
            if data:
                print(f"Name of city received: {data.decode()}")
                city = data.decode()
                if city: 
                    weather = weather_data[city]
                    response = f"Weather information for {city}:\nTemperature: {weather['temperature']}°C\nHumidity: {weather['humidity']}%\nDescription: {weather['description']}"
                    client_socket.sendall(response.encode())
                else:
                    response = f"City not found: {city}"
                    client_socket.sendall(response.encode())
                client_socket.close()
            else:
                print("No data received from client.")