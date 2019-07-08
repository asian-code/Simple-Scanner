#!/usr/bin/python3

import os
import time

os.system("rm -rf /usr/share/simple-scan")  # folder
os.system("rm /usr/share/applications/simplescan.desktop")  # desktop file
os.system("rm /usr/bin/simplescan.sh")  # bash file
time.sleep(3)
print("[+] Uninstall is complete")
