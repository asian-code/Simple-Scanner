
![logo](http://i65.tinypic.com/6swdx0.jpg)
------------------------------------------------------------------------

##   About Simple Scanner  :alien:

This is a small tool which allows for easy accessability to spoofing your MAC Address and scanning IP addresses.
The idea behind this is to help you obtain free airplane wifi.

'<addr>'
Authors and contibutors are not responsible for whatever you do with this tool. <br>
You are responsible for your own actions!


##  Requirements &nbsp; :unlock:

Operating System:
* ![Mac OS X](www.apple.com)
* Linux (Debian/Ubuntu Based: Preferably ![Kali Linux](www.kali.org))

Packages:
* ![arp-scan](https://linux.die.net/man/1/arp-scan)
* ![macchanger](https://github.com/alobbs/macchanger)
* ![nmap](https://nmap.org/)
* ![ipcalc](https://linux.die.net/man/1/ipcalc)
* ![aircrack-ng](https://www.aircrack-ng.org/)
* ![tcpdump](https://www.tcpdump.org/)

Python Library (Pip3):
* python3
* pip3
* ![os](https://docs.python.org/3/library/os.html)
* ![getmac](https://pypi.org/project/getmac/) >= 0.8.1
* ![platform](https://docs.python.org/3/library/platform.html)
* ![scapy](https://pypi.org/project/scapy-python3/)
* ![lanscan](https://pypi.org/project/lanscan/)


## How to Install &nbsp; :inbox_tray:

You can install the program by:

**1. Downloading the file on the Github page**

Or by...

**2. Typing in your terminal - `git clone https://www.github.com/asian-code/airline-crack`**

*Once finished installing, please type `sudo python3 setup.py` to setup your program.*


## :fire: &nbsp; How to Run &nbsp; :fire:

***For Mac OS X:***

Open the directory to the file: 'airline-crack' and run the program by typing: 
`sudo python3 airlinecrack.py`

***For Linux:***

Simply type `airline-crack` in your terminal to run the program.

##### Setup Information

During setup for Linux users, the python program _(core.py and airlinecrack.py)_ will go into the directory: `/usr/share/airline-crack`

As for the bash program, that will allow for running the program with the command 'airline-crack', will go to the directory: `/usr/bin`

This however does not work for Mac OS users as the `/usr/bin/` and `/usr/share` ***is not*** accessable even with sudo.
This is because Macs limit the power of the root account, so that even if you become root, you don't have full control over the system.


