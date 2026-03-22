import requests
import json
import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Warna Hijau Tebal ala Zexr01
G = Fore.GREEN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
R = Fore.RED + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT

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

def track_ip():
    banner()
    print(f"{W}[{G}!{W}] Masukkan Alamat IP Target (Atau kosongkan untuk IP sendiri)")
    target = input(f"{W}➔ {G}")
    
    print(f"\n{W}[{Y}*{W}] Menghubungi Satelit OSINT...")
    time.sleep(1)

    try:
        # API Geolocation (Tanpa Key biar praktis)
        url = f"http://ip-api.com/json/{target}?fields=66846719"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data['status'] == 'fail':
            print(f"{R}[X] Error: Alamat IP tidak valid atau tidak ditemukan!")
            return

        print(f"\n{G}╔═════════════════[ DATA TARGET ]═════════════════╗")
        print(f"{G}║ {W}IP ADDRESS   : {C}{data.get('query')}")
        print(f"{G}║ {W}NEGARA       : {C}{data.get('country')} ({data.get('countryCode')})")
        print(f"{G}║ {W}KOTA/REGION  : {C}{data.get('city')}, {data.get('regionName')}")
        print(f"{G}║ {W}ISP/PROVIDER : {C}{data.get('isp')}")
        print(f"{G}║ {W}ORGANISASI   : {C}{data.get('org')}")
        print(f"{G}║ {W}TIMEZONE     : {C}{data.get('timezone')}")
        print(f"{G}║ {W}KOORDINAT    : {Y}{data.get('lat')}, {data.get('lon')}")
        print(f"{G}║ {W}MAPS LINK    : {G}https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
        print(f"{G}╚═════════════════════════════════════════════════╝")
        
        print(f"\n{G}[+] Scan Selesai. Data berhasil ditarik, Bos!")

    except requests.exceptions.ConnectionError:
        print(f"{R}[X] Error: Cek koneksi internet Abang dulu!")
    except Exception as e:
        print(f"{R}[X] Error Terjadi: {e}")

if __name__ == "__main__":
    try:
        track_ip()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Keluar... Sampai jumpa, Bos!")
              
