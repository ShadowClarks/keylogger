# 🔐 Encrypted Keylogger PoC (Educational Use Only)

![License](https://img.shields.io/github/license/ShadowClarks/keylogger)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Issues](https://img.shields.io/github/issues/ShadowClarks/keylogger)
![Stars](https://img.shields.io/github/stars/ShadowClarks/keylogger?style=social)

This is a **Proof of Concept (PoC)** keylogger built with Python for **educational and ethical** purposes. It captures keystrokes, encrypts them using `cryptography`, and simulates exfiltration to a local server. The goal is to demonstrate secure logging, encryption, and basic persistence techniques.

---

## 🚀 Project Features

- 🔑 Captures keystrokes as **whole words**
- 🔒 Encrypts logs using `Fernet` (symmetric AES encryption)
- 🕒 Saves logs every second with timestamps
- 📤 Simulates exfiltration to a **localhost** server
- 🧱 Kill switch support (`kill.switch` file stops logger)
- 🧠 CLI-based and lightweight
- 🛠️ Startup persistence (auto-start)

---

## 🧰 Tools & Technologies

- Python 3.13
- `pynput` for keyboard capture
- `cryptography` for encryption
- `socket` for simulated exfiltration
- Shell scripts for automation
- Fully modular folder structure

---

## 📁 Folder Structure

```
.
├── decrypt_logs.py               # Decrypt and view log content
├── logger/                      # Core modules
│   ├── key_capture.py
│   ├── encryptor.py
│   └── exfiltrator.py
├── logs/                        # Encrypted logs stored here
├── main.py                      # Starts keylogger and exfiltrator
├── simulate_server.py           # Localhost exfiltration simulation
├── utils/                       # Configs and persistence
│   ├── config.py
│   ├── persistence.py
│   └── secret.key
├── run_logger.sh                # Shell script to start keylogger
├── run_server.sh                # Shell script to start local server
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the local simulated server
```bash
bash run_server.sh
```

### 3. Run the keylogger
```bash
bash run_logger.sh
```

### 4. Decrypt the logs
```bash
python3 decrypt_logs.py
```

---

## 🛑 Kill Switch

To stop the logger at any time, create a file named:

```
kill.switch
```

The script will detect it and exit gracefully.

---

## ⚠️ Disclaimer

> This tool is developed **strictly for educational** and ethical cybersecurity training.  
> **Do not use it to monitor devices without full legal consent.**  
> Misuse can be illegal and punishable under cybercrime laws.  
> The developer holds no responsibility for unethical use.

---

## 🧠 Author

**Akshat Soni (ShadowClarks)**  
Cybersecurity enthusiast | Python developer  
LinkedIn: https://www.linkedin.com/in/akshat-soni-8a98082b5/

---

## 📌 License

MIT License — see `LICENSE` file for details.