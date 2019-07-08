#!/usr/bin/python

import scanclients

rr = '\033[0m'     #reset
bold = '\033[01m'
d = '\033[02m'     #disable
ul = '\033[04m' #underline
reverse = '\033[07m'
st = '\033[09m' #strikethrough
invis = '\033[08m'#invisible
white = '\033[0m'
cwhite = '\33[37m'
black ='\033[30m'
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
 _____ _                 _        _____                 
/  ___(_)               | |      /  ___|                
\ `--. _ _ __ ___  _ __ | | ___  \ `--.  ___ __ _ _ __  
 `--. \ | '_ ` _ \| '_ \| |/ _ \  `--. \/ __/ _` | '_ \ 
/\__/ / | | | | | | |_) | |  __/ /\__/ / (_| (_| | | | |
\____/|_|_| |_| |_| .__/|_|\___| \____/ \___\__,_|_| |_|
                  | |                                   
                  |_|                              
    """)
    print(rr + "[" + lcyan + bold + "1" + rr + "] - " + lcyan + "Scan IPs/Devices on Network")

def clear():
  x = 0
  while x <= 4:
    os.system("clear")

def quit():
  clear()
  exit()

def options():
    try:
      while True:
        answer = input("SimpleScan > ")
        if answer == "1":
          scanclients.scan(ip)
        elif answer == "exit" or answer == "quit":
          quit()
        else:
          clear()
          logo()
          options()
    except:
      quit()
