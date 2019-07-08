#!/usr/bin/python3

import os
import time

os.system("sudo mv skybreak /usr/share")# folder
os.system("sudo mv skybreak.desktop /usr/share/applications/")#.desktop file
os.system("sudo mv skyBREAK /usr/bin")#bash file
time.sleep(3)
print("[+] Setup is complete")
