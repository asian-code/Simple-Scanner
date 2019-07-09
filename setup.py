#!/usr/bin/python3

import os
import time

had_error = False
try:
    os.system("pip3 install scapy")

    os.system("sudo mv simple-scan /usr/share")  # folder
    print("[+] moved simple-scan folder to /usr/share")

    os.system("sudo mv simplescan.desktop /usr/share/applications/")  # .desktop file
    print("[+] moved desktop to /usr/share/applications")

    os.system("sudo mv simplescan /usr/bin")  # bash file
    print("[+] moved bash file to /usr/bin")

    time.sleep(3)

except:
    had_error = True
    raise
finally:
    if had_error:
        print("[-] Setup Failed ")
    else:
        print("[+] Setup is finished,\nyou may run the program by typing : simplescan\nin the terminal)
