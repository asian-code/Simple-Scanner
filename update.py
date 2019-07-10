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
    # uninstalls current version
    subprocess.call("sudo python3 uninstaller.py", shell=True)

    # installs new version
    # subprocess.call("cd {}".format(new_location), shell=True)
    print("installing from github Python message")
    # subprocess.call("git clone https://github.com/asian-code/Simple-Scanner.git",shell=True)  # move downloaded file to original location
    subprocess.call("./gitAddress", shell=True)
    time.sleep(2)
    print("installed the latest version of Simplescanner")
    # curr_location = get_current_dir()
    # print("current location:" + curr_location)

    # os.chmod(location, os.stat.S_IXUSR | os.stat.S_IXGRP | os.stat.S_IXOTH) # chmod

    # subprocess.call("sudo python3 setup.py", shell=True)#setup new version
except:
    had_error = True

finally:
    if had_error:
        print("[!] Error updating Simple-Scanner")
    else:
        print("[+] Update complete,\n")
