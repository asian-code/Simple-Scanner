#!/usr/bin/python
import scapy.all as scapy
import sys

# reference to TCP flags in packet
SynAck = 0x12
RstAck = 0x14


def ping_target(ip, verbose=True):
    scapy.conf.verb = 0
    try:
        ping = scapy.sr1(scapy.IP(dst=ip) / scapy.ICMP())
        if verbose:
            print("[+] Target is online")
        return True
    except Exception:
        if verbose:
            print("[!] Couldn't find target")
        return False


def scan_port(port_to_scan, device_ip):
    srcport = scapy.RandShort()
    SYNACK_packet = scapy.sr1(
        scapy.IP(dst=device_ip) / scapy.TCP(sport=srcport, dport=port_to_scan, flags="S", verbose=False))
    pkt_flags = SYNACK_packet.getlayer(scapy.TCP).flags
    if pkt_flags == SynAck:
        Rst_packet = scapy.IP(dst=device_ip) / scapy.TCP(sport=srcport, dport=port_to_scan, flags="R")
        scapy.send(Rst_packet)
        return True
    else:
        return False


# port scan 20 - 65535
def main():
    try:
        target = input("[*] Enter target IP >")
        min_port = int(input("[*] Enter min port number >"))
        max_port = int(input("[*] Enter mac port number >"))

        if min_port < 0 or max_port < 0 or max_port < min_port:
            print("[!] Invalid Range of Ports")
            sys.exit()

        ports = range(min_port, max_port + 1)

        if ping_target(target) is False:
            sys.exit()

        for port in ports:
            print("[+] Checking " + str(port), end="\r")
            status = scan_port(port, target)
            if status:
                print("Port {} is Open".format(str(port)))
        print('[+] Scan Complete')

    except KeyboardInterrupt:
        print("[+] Exiting program")
        sys.exit()
