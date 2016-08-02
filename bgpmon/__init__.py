def main():
	try: from suds.client import Client
	except: print("Requires suds (suds-jurko)");exit(0)
	self.url="https://api.bgpmon.net/soap/server.php?wsdl"
	self.client=Client(self.url)
