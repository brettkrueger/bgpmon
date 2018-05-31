#!/usr/bin/python
# https://fedorahosted.org/suds/wiki/Documentation
# https://docs.python.org/2/library/unittest.html
# https://portal.bgpmon.net/bgpmonapi.php
try: from bgpmon import *
except: print("Failed to import")
email='demo@bgpmon.net'
passwd='demo'

ip="103.201.129.0/24"
bgpmon=BGPMon()
print("\ngetIpInfo():\n"+str(bgpmon.getIpInfo(email,passwd,ip)))
print("\ngetASName():\n"+str(bgpmon.getASName(email,passwd,"AS134829")))
print("\ngetPrefixesForAS():\n"+str(bgpmon.getPrefixesForAS(email,passwd,int(134829))))
print("\ngetCountry():\n"+str(bgpmon.getCountry(email,passwd,"103.201.129.0")))
print("\ngetUpstreamInfo():\n"+str(bgpmon.getUpstreamInfo(email,passwd,ip,"AS134829")))
print("\ngetUpstreamInfoExtensive():\n"+str(bgpmon.getUpstreamInfoExtensive(email,passwd,ip,"AS134829")))
print("\ngetPrefixes():\n"+str(bgpmon.getPrefixes(email,passwd)))
print("\ninsertPrefix(): Not yet tested\n")
print("\nupdatePrefix(): Not yet tested\n")
print("\ndeletePrefix(): Not yet tested\n")
print("\ngetPrefixUpstreamList():\n"+str(bgpmon.getPrefixUpstreamList(email,passwd,int(1846488))))
print("\naddPrefixUpstreamAS(): Not yet tested\n")
print("\ndeletePrefixUpstreamAS(): Not yet tested\n")
print("\ngetPrefixAdditionalOriginList():\n"+str(bgpmon.getPrefixAdditionalOriginList(email,passwd,int(1846488))))
print("\naddPrefixAdditionalOriginAS(): Not yet tested\n")
print("\ndeletePrefixAdditionalOriginAS(): Not yet tested\n")
print("\ngetAlerts():\n"+str(bgpmon.getAlerts(email,passwd,int(1))))
print("\ngetAlertDetails():\n"+str(bgpmon.getAlertDetails(email,passwd,int(1))))
