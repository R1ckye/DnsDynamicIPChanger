# -*- coding: utf-8 -*-
# Python

import time
from urllib import urlopen
myLastIp = ""
while 1:
	try:
		myIp = urlopen("http://myip.dnsdynamic.org/").read()	# Don't change this!!!
		if myIp != myLastIp:
			myLastIp = myIp
			url = "https://username:password@www.dnsdynamic.org/api/?hostname=yourHostName&myip="	# Change username, password and hostname! (Username is email address)
			url += myIp
			urlopen(url)
	except:
		print "No internet connection!"
	time.sleep(2)	# Change to modify how often the program should check your IP