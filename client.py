import os
import socket

def echo_client(server_host, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.connect((server_host, server_port))
            print(f"Connected to server {server_host}:{server_port}")

            message = 'Hello, this is an echo test!'
            s.sendall(message.encode())

            response = s.recv(1024)
            print(f"Response received from server: {response.decode()}")
    except socket.timeout:
        print("Connection timed out. Server may not be available.")
    except socket.gaierror:
        print(f"Failed to connect to {server_host}. Error with server address or network.")

if __name__ == "__main__":
    server_host = os.getenv('SERVER_HOST', 'echonet-server-service.default.svc.cluster.local')
    server_port = int(os.getenv('SERVER_PORT', 65432))
    echo_client(server_host, server_port)
