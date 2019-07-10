#!/usr/bin/python
import subprocess
import os
import sys
had_error = False
try:
    if os.path.exists("location.txt") == False:
        raise Exception("Missing location.txt file")
    else:
        print("location.txt is good")
except:
    print("[!] Error -Simple scan was never properly installed to update,\n\tMissing location.txt file")
    sys.exit()

file = open("location.txt", "r")
location = file.readlines()[0]  # original location
file.close()

old_location = location.split("/")
old_location.pop()  # remove last element
old_location.pop(0)  # remove first element

new_location = ""
for i in old_location:
    new_location += "/{}".format(i)

# print(new_location)
try:
    # uninstalls current version
    subprocess.call("sudo python3 uninstaller.py", shell=True)
    # installs new version
    subprocess.call("cd {}".format(new_location), shell=True)
    subprocess.call("git clone https://github.com/asian-code/Simple-Scanner.git", shell=True)

    subprocess.call("cd {}".format(location), shell=True)
    # Add chmod +x *
    # run setup.py
except:
    had_error = True

finally:
    if had_error:
        print("[!] Error updating Simple-Scanner")
    else:
        print("[+] Update complete,\n")
