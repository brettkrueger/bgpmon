#!/usr/bin/python
# https://fedorahosted.org/suds/wiki/Documentation
# https://docs.python.org/2/library/unittest.html
# https://portal.bgpmon.net/bgpmonapi.php
try: from bgpmon import *
except: print("Failed to import")
email='demo@bgpmon.net'
passwd='demo'

ip="104.16.0.0/12"
bgpmon=BGPMon()
test=bgpmon.getIpInfo(email,passwd,ip)
print test[0]["prefix"]
