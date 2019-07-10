#!/usr/bin/python
import subprocess
import os, time
import sys

had_error = False
original_location = ""

try:
    if os.path.exists("location.txt") == False:
        raise Exception("Missing location.txt file")
    else:
        print("location.txt is located")
except:
    print("[!] Error -Simple scan was never properly installed to update,\n\tMissing location.txt file")
    sys.exit()

file = open("location.txt", "r")
location = file.readlines()[0]
file.close()

old_location = location.split("/")
old_location.pop(0)  # remove first element (empty element)
original_location = old_location.pop()  # remove last element (name of installation folder)
print("pop of last element :"+original_location)

install_location = ""
for i in old_location:
    install_location += "/{}".format(i)

original_location = install_location + "/" + original_location

print("[+] Original file location:" + original_location + "[+] Location to install: " + install_location)
try:
    # installs new version
    subprocess.call("./gitAddress", shell=True)
    time.sleep(2)
    print("[ OK ] Installed new version of Simple-Scanner")

    # uninstalls current version
    print("[+] Uninstalling old version of Simple Scanner")
    subprocess.call("sudo python3 uninstaller.py", shell=True)

    # move new version to the location of old installation folder
    print("moving new installation folder to old installation folder location")
    subprocess.call("sudo mv /usr/var/Simple-Scanner {}".format(install_location), shell=True)

    # os.chmod(location, os.stat.S_IXUSR | os.stat.S_IXGRP | os.stat.S_IXOTH)  # chmod

    subprocess.call("sudo python3 {}/setup.py".format(original_location), shell=True)  # setup new version
    time.sleep(2)
except:
    had_error = True

finally:
    if had_error:
        print("[!] Error updating Simple-Scanner")
    else:
        print("[ OK ] Update complete!!\n")
