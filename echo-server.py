import socket

def echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Serverul ascultă la {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"Conectat de la {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    echo_server('0.0.0.0', 65432)
