from cryptography.fernet import Fernet
from utils.config import ENCRYPTION_KEY

class Encryptor:
    def __init__(self):
        self.fernet = Fernet(ENCRYPTION_KEY)

    def encrypt(self, data: str) -> bytes:
        return self.fernet.encrypt(data.encode())

    def decrypt(self, token: bytes) -> str:
        return self.fernet.decrypt(token).decode()
