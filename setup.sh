#!/bin/bash
# Warna
G='\033[1;32m'
W='\033[1;37m'
N='\033[0m'

echo -e "${G}[*] Menginstall bahan-bahan Z-IP-Tracker...${N}"
pkg update && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt

echo -e "${G}[*] Memberikan izin eksekusi...${N}"
chmod +x Z-IP.py

echo -e "${G}[*] Selesai! Kamu bisa jalankan dengan ketik: python Z-IP.py${N}"

