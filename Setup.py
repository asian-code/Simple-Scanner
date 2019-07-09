#!/usr/bin/python3

import os
import time

os.system("sudo mv simple-scan /usr/share")# folder
print("[+] moved simple-scan folder to /usr/share")
os.system("sudo mv simplescan.desktop /usr/share/applications/")#.desktop file
print("[+] moved desktop to /usr/share/applications")
os.system("sudo mv simplescan /usr/bin")#bash file
print("[+] moved bash file to /usr/bin")
time.sleep(3)
print("[+] Setup is complete")
