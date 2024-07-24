import socket

def echo_client(server_host, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        print(f"Conectat la serverul {server_host}:{server_port}")

        message = 'Salut, acesta este un test de echo!'
        s.sendall(message.encode())

        response = s.recv(1024)
        print(f"Raspuns primit de la server: {response.decode()}")

if __name__ == "__main__":
    echo_client('host.docker.internal', 65432)
