
![logo](http://i65.tinypic.com/6swdx0.jpg)

##   About Simple Scanner  :alien:

This is a small tool which allows for easy accessability to spoofing your MAC Address(feature coming soon) and scanning IP addresses.
The idea behind this is to help you obtain free airplane,hotel,etc wifi.


##Authors and contibutors are not responsible for whatever you do with this tool. <br>
##You are responsible for your own actions!

## How to use :question:
 * The program takes in terminal arguments (not required to run). <br>
 example :  `python3 networkscanner.py -t 192.168.0.5`<br> 
 or `python3 networkscanner.py --target 192.168.0.5` 
 

##  Requirements &nbsp; :unlock:

Operating System:
* ![Mac OS X](www.apple.com)
* Linux (Debian/Ubuntu Based: Preferably ![Kali Linux](www.kali.org))

Python Library (Pip3):
* python3
* pip3
* ![os](https://docs.python.org/3/library/os.html)
* ![scapy](https://pypi.org/project/scapy-python3/)



## How to Install :inbox_tray:

You can install the program by:

**1. Downloading the file on the Github page**

Or by...

**2. Typing in your terminal - `git clone https://github.com/asian-code/Simple-Scanner`**

*Once finished installing, please type `sudo python3 setup.py` to setup your program.*


## How to Run &nbsp; :fire:

Open the directory to the file: 'simple-scanner' and run the program by typing: 
`sudo python3 networkScanner.py`


##### Setup Information

During setup for Linux users, the python program _(core.py and networkScanner.py)_ will go into the directory: `/usr/share/simple-scanner`

As for the bash program, that will allow for running the program with the command 'simple-scanner', will go to the directory: `/usr/bin`

This however does not work for Mac OS users as the `/usr/bin/` and `/usr/share` ***is not*** accessable even with sudo.
This is because Macs limit the power of the root account, so that even if you become root, you don't have full control over the system.

## Troubleshooting :skull:
* **If you are unsure of the arguments in the program, locate the `networkscanner.py` file <br>and type in terminal `python3 networkscanner.py -help` for info on how to use the program** 
