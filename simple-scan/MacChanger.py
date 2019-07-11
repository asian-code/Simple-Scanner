#!/usr/bin/python
import subprocess  # cmd commands module
import optparse  # external input with script through cmd EXAMPLE: macChanger.py -i eth0 -m 00:11:22:33:44:55
import re  # regular expression
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'

# my Original mac eth0: 08:00:27:89:03:db

def show_info(interface="None", new_mac="None"):
    txt = green+bold+"--------------------------------- \n" \
          "| Interface  >  {}\n" \
          "| New Mac    >  {}\n" \
          "--------------------------------- \n"+rr
    print(txt.format(interface, new_mac))


def change_mac(interface, new_mac):
    print("[+] Changing " + interface + " MAC to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_args():  # returns all the values that are used in Cmd
    parser = optparse.OptionParser()  # object
    parser.add_option("-i", "--interface", dest="inface", help="Network adaptor to change MAC")
    parser.add_option("-m", "--mac", dest="nmac", help="The new MAC address to change to")
    (options, arguments) = parser.parse_args()  # contains a tuple

    show_info(options.inface, options.nmac)

    # Program can run with/without parse
    if not options.inface:
        print("[-] Missing interface ")
        options.inface = input("Interface >")
    if not options.nmac:
        print("[-] Missing new MAC address")
        options.nmac = input("New MAC >")
    return options


def get_mac(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", interface])
    search_results = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_results))

    if search_results:
        return search_results.group(0)

    return None


def main():
    value = get_args()
    old_mac = get_mac(value.inface)
    if old_mac:
        print(" Current MAC address > " + get_mac(value.inface))
        change_mac(value.inface, value.nmac)
        if old_mac == get_mac(value.inface):
            print(red+bold+"[-] Error Changing the MAC address, Old MAC and new MAC are the same"+rr)
        else:
            print(green+bold+"[ OK ] Change Complete "+rr)
    else:
        print(red+bold+"[!] Error - Could not find MAC address for this interface"+rr)

# print(type(get_args()))
