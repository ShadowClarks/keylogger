import os
from cryptography.fernet import Fernet

# Generate or load encryption key
KEY_FILE = "utils/secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

# Encryption key
ENCRYPTION_KEY = load_key()

# Path to store logs
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Kill switch file
KILL_SWITCH_FILE = "utils/kill.switch"

# Simulated server details
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999
