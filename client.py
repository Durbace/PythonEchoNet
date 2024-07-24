import os
import socket

def echo_client(server_host, server_port):
    running_in_docker = os.getenv('RUNNING_IN_DOCKER') == 'true'

    if not running_in_docker:
        server_host = '127.0.0.1' 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        print(f"Conectat la serverul {server_host}:{server_port}")

        message = 'Salut, acesta este un test de echo!'
        s.sendall(message.encode())

        response = s.recv(1024)
        print(f"Raspuns primit de la server: {response.decode()}")

if __name__ == "__main__":
    echo_client('host.docker.internal' if os.getenv('RUNNING_IN_DOCKER') == 'true' else '127.0.0.1', 65432)


