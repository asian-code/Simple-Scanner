#!/usr/bin/python
import scapy.all as scapy
import sys

red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
lblue = '\033[94m'
# reference to TCP flags in packet
SynAck = 0x12
RstAck = 0x14
open_ports = []  # all open port for current target


def ping_target(ip, verbose=True):
    scapy.conf.verb = 0
    try:
        ping = scapy.sr1(scapy.IP(dst=ip) / scapy.ICMP())
        if verbose:
            print(green + bold + "[+] " + str(ip) + " is online" + rr)
        return True
    except Exception:
        if verbose:
            print(red + bold + "[!] Couldn't find " + rr + ip)
        return False


def scan_port(device_ip, port_to_scan):
    srcport = scapy.RandShort()
    SYNACK_packet = scapy.sr1(scapy.IP(dst=device_ip) / scapy.TCP(sport=srcport, dport=port_to_scan, flags="S"),
                              timeout=.008)  # packet with sync flag

    if SYNACK_packet is None:  # if there are no response
        return False
    pkt_flags = SYNACK_packet.getlayer(scapy.TCP).flags  # get flag

    if pkt_flags == SynAck:
        Rst_packet = scapy.IP(dst=device_ip) / scapy.TCP(sport=srcport, dport=port_to_scan,
                                                         flags="R")  # packet with reset flag
        scapy.send(Rst_packet)
        return True
    else:
        return False


# port scan 0 - 65535
# gunna scan from 15 - 8080
def main(devices_to_scan: list):
    min_port = 100
    # min_port = 15
    # max_port = 50000
    max_port = 150
    try:
        for target in devices_to_scan:
            # if min_port < 0 or max_port < 0 or max_port < min_port:
            #     print("[!] Invalid Range of Ports")
            #     sys.exit()

            ports = range(min_port, max_port + 1)

            if ping_target(target) is False:
                break
            open_ports = []
            for port in ports:
                print("[+] Checking " + str(port), end="")
                if scan_port(target, port):
                    print("\rPort {} is Open".format(str(port)))
                    open_ports.append(str(port))
                print("\r", end="")
            print('[+] Scan Complete' + open_ports)

    except KeyboardInterrupt:
        print("[+] Exiting program")
        sys.exit()
    except:
        print("[!] Error ")
        raise


main(["10.0.0.0", "10.0.2.2"])
