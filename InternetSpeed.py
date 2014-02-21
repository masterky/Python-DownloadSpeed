import urllib2
from datetime import datetime
def measure(url="http://hr.releases.ubuntu.com/jaunty/ubuntu-9.04-desktop-i386.iso", intervall=3, buf=10):
	f = urllib2.urlopen(url)
	tStart = datetime.now()
	amount = 0
	while f.read(buf) is not None:
		tEnd = datetime.now()
		dif = (tEnd - tStart).total_seconds()
		#print dif
		if (dif >= intervall):
			print (amount/intervall)/1000, " Kb/s"
			amount = 0
			tStart = datetime.now()
		else:
			amount = amount + buf
		#print amount

try:
	measure(url="http://hr.releases.ubuntu.com/jaunty/ubuntu-9.04-desktop-i386.iso", buf=1000, intervall=3)
except KeyboardInterrupt:
	exit(0)