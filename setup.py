#!/usr/bin/python3


import time
import subprocess

had_error = False
try:
    subprocess.call("pip3 install scapy", shell=True)

    subprocess.call("sudo mv simple-scan /usr/share", shell=True)  # folder
    print("[+] moved simple-scan folder to /usr/share")

    subprocess.call("sudo mv simplescan.desktop /usr/share/applications/", shell=True)  # .desktop file
    print("[+] moved desktop to /usr/share/applications")

    subprocess.call("sudo mv simplescan /usr/bin", shell=True)  # bash file
    print("[+] moved bash file to /usr/bin")

    # get current direcotry
    save_location = str(subprocess.check_output(["pwd"]))
    # save directory to file in the folder
    # delete this folder later in uninstaller.py
    folder = save_location.split("/")
    folder.remove("b'")  # this is needed to remove the first element in the list
    folder[len(folder) - 1] = folder[len(folder) - 1].split("\\")[0]
    for i in folder:
        print(i)
    # print(save_location)
    time.sleep(3)
except:
    had_error = True
    raise
finally:
    if had_error:
        print("[-] Setup Failed, an error stopped the setup process ")
    else:
        print("[+] Setup is complete, no errors!")
