#!/usr/bin/python
import scapy.all as scapy
import sys
from datetime import datetime

try:
    target = input("[*] Enter target IP >")
    min_port = int(input("[*] Enter min port number >"))
    max_port = int(input("[*] Enter mac port number >"))
    try:
        if min_port >= 0 and max_port >= 0 and max_port > min_port:
            pass
        else:
            raise Exception()
    except Exception:
        print("[!] Invaild Range of Ports")
        sys.exit()
except KeyboardInterrupt:
    print("[+] Exiting program")
    sys.exit()

ports = range(min_port, max_port + 1)
start_clock = datetime.now()
SynAck = 0x12
RstAck = 0x14


def ping_host(ip):
    scapy.conf.verb = 0
    try:
        ping = scapy.sr1(scapy.IP(dst=ip) / scapy.ICMP())
        print("[+] Target is online")
        return True
    except Exception:
        print("[!] Couldnt find target")
        return False


def scan_port(port_to_scan):
    srcport = scapy.RandShort()
    SYNACK_packet = scapy.sr1(
        scapy.IP(dst=target) / scapy.TCP(sport=srcport, dport=port_to_scan, flags="S", verbose=False))
    pkt_flags = SYNACK_packet.getlayer(scapy.TCP).flags
    if pkt_flags == SynAck:
        Rst_packet = scapy.IP(dst=target) / scapy.TCP(sport=srcport, dport=port_to_scan, flags="R")
        scapy.send(Rst_packet)
        return True
    else:
        return False


if ping_host(target) is False:
    sys.exit()
print("[+] Scanning started at {}!\n".format(datetime.strftime("%H:%M:%S")))

for port in ports:
    print("[+] Checking " + str(port), end="\r")
    status = scan_port(port)
    if status:
        print("Port {} is Open".format(str(port)))
stop_clock = datetime.now()
total_time = stop_clock - start_clock
print('[+] Scan Complete, Total scan time:' + str(total_time))
