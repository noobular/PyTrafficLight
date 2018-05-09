"""
INSTRUCTIONS
	1.)
		git clone https://github.com/simonmonk/squid.git
	2.)
		cd squid
	3.)
		sudo python3 setup.py install
"""
from squid import *
from time import sleep

TLight = Squid(18,23,24)
while True:
    TLight.set_color(GREEN)
    sleep(2)
    TLight.set_color(YELLOW)
    sleep(2)
    TLight.set_color(RED)
    sleep(2)
    
