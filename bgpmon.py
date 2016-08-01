class BGPMon():
	def __init__(self):
		try: from suds.client import Client
		except: print("Requires suds (suds-jurko)");exit(0)
		self.url="https://api.bgpmon.net/soap/server.php?wsdl"
		self.client=Client(self.url)

	def addPrefixAdditionalOriginAS(self,email,passwd,prefix,origin):
		return self.client.service.addPrefixAdditionalOriginAS(email,passwd,prefix,origin)

	def addPrefixUpstreamAS(self,email,passwd,prefix,upstream):
		return self.client.service.addPrefixUpstreamAS(email,passwd,prefix,origin)

	def deletePrefix(self,email,passwd,prefix):
		return self.client.service.deletePrefix(email,passwd,prefix)

	def deletePrefixAdditionalOriginAS(self,email,passwd,prefix,origin):
		return self.client.service.deletePrefixAdditionalOriginAS(email,passwd,prefix,origin)

	def getASName(self,email,passwd,int_as):
		return self.client.service.getASName(email,passwd,int_as)
	
	def getAlertDetails(self,email,passwd,alert):
		return self.client.service.getAlertDetails(email,passwd,alert)

	def getAlerts(self,email,passwd,days):
		return self.client.service.getAlerts(email,passwd,days)	

	def getCountry(self,email,passwd,ip):
		return self.client.service.getCountry(email,passwd,ip)

	def getIpInfo(self,email,passwd,ip):
		return self.client.service.getIpInfo(email,passwd,ip)
	
	def getPrefixAdditionalOriginList(self,email,passwd,prefix):
		return self.client.service.getPrefixAdditionalOriginList(email,passwd,prefix)

	def getPrefixUpstreamList(self,email,passwd,prefix):
		return self.client.service.getPrefixUpstreamList(email,passwd,prefix)

	def getPrefixes(self,email,passwd):
		return self.client.service.getPrefixes(email,passwd)

	def getPrefixesForAS(self,email,passwd,int_as):
		return self.client.service.getPrefixesForAS(email,passwd,int_as)

	def getUpstreamInfo(self,email,passwd,prefix,src):
		return self.client.service.getUpstreamInfo(email,passwd,prefix,src)
		
	def getUpstreamInfoExtensive(self,email,passwd,prefix,src):
		return self.client.service.getUpstreamInfoExtensive(email,passwd,prefix,src)

	def insertPrefix(self,email,passwd,base,prefix,prefix_length,ignore_morespec,peer_threshold,peer_threshold_withdraw,must_match,check_roa,notify_withdraw,regex,description):
		notitfy_withdraw=notify_withdraw
		return self.client.service.insertPrefix(email,passwd,base,prefix,prefix_length,ignore_morespec,peer_threshold,peer_threshold_withdraw,must_match,check_roa,notitfy_withdraw,regex,description)

	def updatePrefix(self,email,passwd,base,prefix,ignore_morespec,peer_threshold,peer_threshold_withdraw,must_match,check_roa,notify_withdraw,regex,description):
		notitfy_withdraw=notify_withdraw
		return self.client.service.updatePrefix(email,passwd,base,prefix,ignore_morespec,peer_threshold,peer_threshold_withdraw,must_match,check_roa,notitfy_withdraw,regex,description)
