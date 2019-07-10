#!/usr/bin/python
import subprocess
import os, time
import sys

had_error = False


def get_current_dir():
    save_location = str(subprocess.check_output(["pwd"]))
    # save directory to txt file in the simple-scan folder
    # delete this folder later in uninstaller.py
    folder = save_location.split("/")
    folder.pop(0)  # this is needed to remove the first element in the list
    folder[len(folder) - 1] = folder[len(folder) - 1].split("\\")[0]  # removes the \n in the last element
    result = ""
    for i in folder:
        result += "/" + i
        return result


try:
    if os.path.exists("location.txt") == False:
        raise Exception("Missing location.txt file")
    else:
        print("location.txt is located")
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

print("[+] Location to install: " + new_location)
try:
    # installs new version
    subprocess.call("./gitAddress", shell=True)
    time.sleep(2)

    # uninstalls current version
    print("[+] Uninstalling old version of Simple Scanner")
    subprocess.call("sudo python3 uninstaller.py", shell=True)

    # move new version to the location of old installation folder
    print("moving new installation folder to old installation folder location")
    subprocess.call("sudo mv /usr/var/Simple-Scanner {}".format(new_location), shell=True)
    
    # os.chmod(location, os.stat.S_IXUSR | os.stat.S_IXGRP | os.stat.S_IXOTH) # chmod

    # subprocess.call("sudo python3 setup.py", shell=True)#setup new version
except:
    had_error = True

finally:
    if had_error:
        print("[!] Error updating Simple-Scanner")
    else:
        print("[+] Update complete,\n")
