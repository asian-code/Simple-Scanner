#!/usr/bin/python
import subprocess
import os, time
import sys

had_error = False
original_location = ""
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
try:
    if os.path.exists("location.txt") == False:
        raise Exception("Missing location.txt file")
    else:
        print("location.txt is located")
except:
    print(
        red + bold + "[!] Error -Simple scan was never properly installed to update,\n\tMissing location.txt file" + rr)
    sys.exit()

file = open("location.txt", "r")
location = file.readlines()[0]
file.close()

old_location = location.split("/")
old_location.pop(0)  # remove first element (empty element)
original_location = old_location.pop()  # remove last element (name of installation folder)
original_location = original_location.split("\\")[0]  # removes the \n inside the string

install_location = ""
for i in old_location:
    install_location += "/{}".format(i)

original_location = str(install_location + "/" + original_location)

print(
    green + bold + "[+] Original file location:" + original_location + "\n[+] Location to install: " + install_location + rr)
try:
    # installs new version
    subprocess.call("./gitAddress", shell=True)
    time.sleep(3)
    print(green + bold + "[ OK ] Installed new version of Simple-Scanner" + rr)

    # uninstalls current version
    print("[+] Uninstalling old version of Simple Scanner")
    subprocess.call("sudo python3 uninstaller.py", shell=True)

    time.sleep(2)
    # move new version to the location of old installation folder
    subprocess.call("sudo mv /usr/var/Simple-Scanner {}".format(install_location), shell=True)
    print(green + bold + "[+] Moved new files to correct location" + rr)

    # time.sleep(2)
    # os.chmod(original_location, os.stat.S_IXUSR | os.stat.S_IXGRP | os.stat.S_IXOTH)  # chmod
    # print("TRYING CHMOD")
    # subprocess.call("cd "+original_location, shell=True)
    # subprocess.call("sudo chmod +x *", shell=True)

    time.sleep(4)
    # setup the program for the user
    print("[+] Running setup.py in - {}/setup.py".format(original_location))
    subprocess.call("cd " + original_location)
    print("Current directory:" + subprocess.check_output("pwd"))
    subprocess.call("sudo python3 {}/setup.py".format(original_location), shell=True)  # setup new version

except:
    had_error = True

finally:
    if had_error:
        print(red + bold + "[!] Error updating Simple-Scanner" + rr)
    else:
        print(green + bold + "[ OK ] Update complete!!\n" + rr)
