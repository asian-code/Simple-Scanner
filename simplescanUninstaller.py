#!/usr/bin/python3

import os
import time

had_error = False
try:
    os.system("sudo rm -rf /usr/share/simple-scan")  # folder
    print("[+] removed simple-scan folder in /usr/share/simple-scan")

    os.system("sudo rm -rf /usr/share/applications/simplescan.desktop")  # desktop file
    print("[+] removed desktop file in /usr/share/applications/simplescan.desktop")

    os.system("sudo rm -rf /usr/bin/simplescan")  # bash file
    print("[+] removed bash file /usr/bin/simplescan")

    time.sleep(3)
except:
    had_error = True
    raise
finally:
    if had_error:
        print("[-] Unable to uninstall Simple-scan due to an error")
    else:
        print("[+] Uninstall is complete, no errors !")
