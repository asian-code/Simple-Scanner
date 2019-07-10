#!/usr/bin/python3


import time
import subprocess

had_error = False


def get_current_dir():
    save_location = str(subprocess.check_output(["pwd"]))
    # save directory to txt file in the simple-scan folder
    # delete this folder later in uninstaller.py
    folder = save_location.split("/")
    folder.remove("b'")  # this is needed to remove the first element in the list
    folder[len(folder) - 1] = folder[len(folder) - 1].split("\\")[0]  # removes the \n in the last element
    result = ""
    for i in folder:
        result += "/" + i
    return result


def save_folder_location(location):
    try:
        file = open(location + "/location.txt", "w")
        file.write(location)
    except:
        print("[-] Error writing to file")
        had_error = True
        raise
    finally:
        file.close()


try:
    subprocess.call("pip3 install scapy", shell=True)

    subprocess.call("sudo mv simple-scan /usr/share", shell=True)  # folder
    print("[+] moved simple-scan folder to /usr/share")

    subprocess.call("sudo mv simplescan.desktop /usr/share/applications/", shell=True)  # .desktop file
    print("[+] moved desktop to /usr/share/applications")

    subprocess.call("sudo mv simplescanner /usr/bin", shell=True)  # bash file
    print("[+] moved bash file to /usr/bin")

    save_folder_location(get_current_dir())

    time.sleep(3)
except:
    had_error = True
    raise
finally:
    if had_error:
        print("[-] Setup Failed, an error stopped the setup process ")
    else:
        print("[+] Setup is complete, no errors!")
