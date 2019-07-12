#!/usr/bin/python
import scapy.all as scapy
import optparse, sys

clients = []  # list of devices on network,each element is a Dictionary


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="the device or range of devices to scan")
    options, arguments = parser.parse_args()
    if options.target is None:
        options.target = input("* target examples: 192.168.5.1, 192.168.1.1/24  \n[*] Enter target > ")
    return options.target


def scan(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # broadcast Mac address
    arp_request_packet = broadcast / request  # create ARP request packet
    answered_list = scapy.srp(arp_request_packet, timeout=2, verbose=False)[0]  # send packet to network
    # print(answered_list.summary())
    # print(arp_request_packet.summary())

    print("IP\t\t\tMac Address\n" + ("-" * 50))

    for element in answered_list:  # get the info from list returned from scapy
        client = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients.append(client)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        # print(element[1].show())
    print("-" * 50)


def write_file(trigger):
    if trigger:
        with open("/root/Network_Scan.txt", "w") as file:
            file.write("IP\t\t\tMac Address\n" + ("-" * 50) + "\n")
            for c in clients:
                file.write(c["ip"] + "\t\t" + c["mac"] + "\n")
            file.write("-" * 50 + "\n")
            file.close()
            print("[+] Saved results in > /root/Network_Scan.txt")


def main():
    scan(get_arguments())
    # if user wants to save result to file
    if len(clients) > 0:
        try:
            want_saved = input("[*] Save results to a file? (y/n): ")
            want_saved = want_saved.lower()
            write_file(want_saved == "y" or want_saved == "yes")
        except KeyboardInterrupt:
            # print("\r", end=" ")
            print(print("[-] Closing the application........"))
            pass
        except:
            print("[-] Error writing to file")
            raise  # prints out error message without stopping program
        return clients
