import requests
import json
import os
import sys
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)
G, W, R, C, Y = Fore.GREEN + Style.BRIGHT, Fore.WHITE + Style.BRIGHT, Fore.RED + Style.BRIGHT, Fore.CYAN + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT

def banner():
    os.system('clear')
    print(f"""
{G}███████╗      ██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
{G}╚══███╔╝      ██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
{G}  ███╔╝ █████╗██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
{G} ███╔╝  ╚════╝██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
{G}███████╗      ██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
{G}╚══════╝      ╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
          {W}[ IP GEOLOCATION OSINT BY ZEXR01 - RELAX AJA BRO! ]
    """)

def save_log(data):
    with open("ip_history.txt", "a") as f:
        f.write(f"[{datetime.now()}] IP: {data['query']} - {data['city']}, {data['country']}\n")

def track_ip():
    banner()
    print(f"{W}[{G}INFO{W}] Masukkan IP target (Contoh: 8.8.8.8) atau ENTER untuk IP Anda.")
    target = input(f"{W}Target IP ➔ {G}")
    
    print(f"\n{W}[{Y}*{W}] Menghubungi Server OSINT... {G}[RELAX]")
    time.sleep(1.5)

    try:
        # Request data lengkap (Geolocation + Proxy + Currency)
        url = f"http://ip-api.com/json/{target}?fields=16584703"
        response = requests.get(url, timeout=12)
        data = response.json()

        if data.get('status') == 'fail':
            print(f"{R}[!] Error: {data.get('message', 'IP tidak valid!')}")
            return

        # Tampilan Data Kompleks
        print(f"\n{G}╔═════════════════[ NETWORK INFO ]═════════════════╗")
        print(f"{G}║ {W}IP ADDRESS   : {C}{data.get('query')}")
        print(f"{G}║ {W}ISP/PROVIDER : {C}{data.get('isp')}")
        print(f"{G}║ {W}AS/ASN       : {C}{data.get('as')}")
        print(f"{G}║ {W}STATUS PROXY : {R if data.get('proxy') else G}{'AKTIF (BAHAYA)' if data.get('proxy') else 'BERSIH'}")
        print(f"{G}╠═════════════════[ GEOLOCATION ]══════════════════╣")
        print(f"{G}║ {W}NEGARA       : {C}{data.get('country')} ({data.get('countryCode')})")
        print(f"{G}║ {W}KOTA/REGION  : {C}{data.get('city')}, {data.get('regionName')}")
        print(f"{G}║ {W}KODE POS     : {C}{data.get('zip')}")
        print(f"{G}║ {W}KOORDINAT    : {Y}{data.get('lat')}, {data.get('lon')}")
        print(f"{G}║ {W}TIMEZONE     : {C}{data.get('timezone')}")
        print(f"{G}║ {W}MATA UANG    : {C}{data.get('currency')}")
        print(f"{G}╠═══════════════════[ LIVE MAPS ]══════════════════╣")
        print(f"{G}║ {G}URL: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
        print(f"{G}╚══════════════════════════════════════════════════╝")
        
        save_log(data)
        print(f"\n{G}[✓] Data berhasil disimpan di 'ip_history.txt'")

    except Exception as e:
        print(f"{R}[!] Terjadi Gangguan: {e}")

if __name__ == "__main__":
    try:
        track_ip()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Keluar... Ngopi dulu, Bos! ☕")
