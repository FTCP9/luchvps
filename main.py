import sys
import os
import time
from datetime import datetime
import colorama
from colorama import *
from pypresence import Presence

client_id = '977577659217354813'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

RPC.update(state=f"Something like normal vps", details=f"Using luch vps", large_image="new_piskel_1_", small_image=" ", large_text="Developed by Looph")

def login():
    u = input("login as: ")
    if u == "root":
        p = input("root@ubuntu's password:" + Fore.BLACK + " ")
        if p == "root":
            print(Fore.WHITE + """ 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.162-1-pve x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
 """)
            os.system("title root@ubuntu: ~")
            debil()

def debil():
    sin = input("root@ubuntu ~ # ").lower()
    sinput = sin.split(" ")[0]

    if sinput == "java":
        sinput, asd, kokot, ip, port, method, duration = sin.split(" ")
        if asd == "-jar":
            if kokot == "vip.jar":
                print(f"\nIP: {ip}\nPORT: {port}\nTIME: {duration}\nATTACK STARTED!\n")
                os.system(f"")
                debil()
            if kokot == "team.jar":
                print(f"\nIP: {ip}\nPORT: {port}\nTIME: {duration}\nATTACK STARTED!\n")
                os.system(f"")
                debil()
            if kokot == "normal.jar":
                print(f"\nIP: {ip}\nPORT: {port}\nTIME: {duration}\nATTACK STARTED!\n")
                os.system(f"")
                debil()
        else:
            print("wrong")

    if sinput == "htop":
        print("smrdis")
        debil()

    if sinput == "ls":
        print("bot.jar  infinity.sh  vip.jar  team.jar  normal.jar")
        debil()
    
    if sinput == "./infinity.sh":
        print("infinity is very good stresser")
        debil()

    if sinput == "./infinity":
        print("infinity is very good stresser")
        debil()

    if sinput == "infinity.sh":
        print("infinity is very good stresser")
        debil()
    if sinput == "clear":
        os.system("cls")
        debil()
    if sinput == "lscpu":
        print("""Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                12
On-line CPU(s) list:   24
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 23
Stepping:              7
CPU MHz:               1998.000
BogoMIPS:              4999.98
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              3072K""")
        debil()

    if sinput == "attackstop":
        os.system("java -jar InfinityConnector.jar stop")
        debil()

    if sinput == "authors":
        print("Console Author:\n\nLooph - OWNER\nBrutalCODE - API\n")
        debil()
        
    else:
        print("/etc/bash: "+ sinput +": command not found")
        debil()

os.system("title PuTTY (inactive)")
os.system("cls")
login()