import os
import socket

def echo_client(server_host, server_port):
    try:
        print(f"Attempting to connect to server {server_host}:{server_port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # Set timeout to 10 seconds
            s.connect((server_host, server_port))
            print(f"Connected to server {server_host}:{server_port}")

            message = 'Hello, this is an echo test!'
            s.sendall(message.encode())

            response = s.recv(1024)
            print(f"Response received from server: {response.decode()}")
    except socket.timeout:
        print("Connection timed out. Server may not be available.")
    except socket.gaierror as e:
        print(f"Failed to connect to {server_host}. Error with server address or network: {e}")
        if os.getenv('FALLBACK_LOCALHOST', 'false').lower() == 'true':
            try:
                print(f"Attempting to connect to localhost:{server_port}")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(10)
                    s.connect(('localhost', server_port))
                    print(f"Connected to server localhost:{server_port}")

                    message = 'Hello, this is an echo test!'
                    s.sendall(message.encode())

                    response = s.recv(1024)
                    print(f"Response received from server: {response.decode()}")
            except socket.timeout:
                print("Connection to localhost timed out.")
            except Exception as e:
                print(f"Failed to connect to localhost as well: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    server_host = os.getenv('SERVER_HOST', 'localhost')
    server_port = int(os.getenv('SERVER_PORT', 65432))
    echo_client(server_host, server_port)
