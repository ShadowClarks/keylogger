import socket

HOST = '127.0.0.1'
PORT = 9999

def start_server():
    print(f"[+] Simulated server listening on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"[+] Connection from {addr}")
                buffer = b""
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    buffer += data
                print(f"[*] Received {len(buffer)} bytes.\n---")

if __name__ == "__main__":
    start_server()
