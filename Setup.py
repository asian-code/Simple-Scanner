#!/usr/bin/python3

import os
import time

os.system("sudo mv simple-scan /usr/share")# folder
os.system("sudo mv simplescan.desktop /usr/share/applications/")#.desktop file
os.system("sudo mv simplescan /usr/bin")#bash file
time.sleep(3)
print("[+] Setup is complete")
