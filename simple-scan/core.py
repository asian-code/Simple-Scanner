#!/usr/bin/python

import networkScanner
import os
import sys

rr = '\033[0m'  # reset
bold = '\033[01m'
d = '\033[02m'  # disable
ul = '\033[04m'  # underline
reverse = '\033[07m'
st = '\033[09m'  # strikethrough
invis = '\033[08m'  # invisible
white = '\033[0m'
cwhite = '\33[37m'
black = '\033[30m'
red = '\033[31m'
green = '\033[92m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'


def logo():
    print(lcyan + bold + """
   _____ _                 __          _____                                 
  / ___/(_)___ ___  ____  / /__       / ___/_________ _____  ____  ___  _____
  \__ \/ / __ `__ \/ __ \/ / _ \______\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 ___/ / / / / / / / /_/ / /  __/_____/__/ / /__/ /_/ / / / / / / /  __/ /    
/____/_/_/ /_/ /_/ .___/_/\___/     /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                /_/  Created by asian-code
                   (Special thanks to lin8x)""")
    print(ul+"https://www.github.com/asian-code/Simple-Scanner")

    print(rr + "(" + cyan + bold + "1" + rr + ")\t- " + rr + "Scan IPs/Devices on Network")
    print(rr + "(" + cyan + bold + "2" + rr + ")\t- " + rr + "Scan IPs + Port scanner(Comming soon)")
    print(rr + "(" + cyan + bold + "3" + rr + ")\t- " + rr + "Change Mac address(Comming soon)")
    print(rr + "(" + cyan + bold + "clear" + rr + ")\t- " + rr + "Clear screen")
    print(rr + "(" + cyan + bold + "99" + rr + ")\t- " + rr + "Exit the program")


def clear():
    x = 0
    while x <= 4:
        os.system("clear")
        x += 1


def quit():
    sys.exit()


def options():
    try:
        while True:
            try:
                answer = input(cyan + bold + "Simple-Scanner > " + rr)
                if answer == "1":
                    networkScanner.main()
                elif answer=="2":
                    print(rr + bold + "[-] function comming soon"+rr)
                elif answer == "3":
                    print(rr + bold + "[-] function comming soon"+rr)
                elif answer.lower() == "exit" or answer == "99" or answer.lower()=="quit":
                    quit()
                elif answer=="clear":
                    clear()
                    logo()
                else:
                    print(red + bold + "[-] Invalid command: " +rr+ answer )
            except KeyboardInterrupt:
                quit()
    except KeyboardInterrupt:
        quit()
