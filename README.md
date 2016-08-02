# bgpmon
A Python wrapper for the bgpmon SOAP API.

###How to install
```
pip install bgpmon
```
or
```
git clone https://github.com/brettkrueger/bgpmon.git
cd bgpmon
python setup.py build
python setup.py install
```

###Example usage
```
>>> from bgpmon import *
>>> bgpmon=BGPMon()
>>> print(bgpmon.getIpInfo(email,passwd,"103.201.129.0"))
[(Prefix_info){
   prefix = "103.201.129.0/24"
   prefix_description = "xTom Japan"
   country_code = "unknown"
   origin_as = "134829"
   origin_as_name = "xTom Global Anycast Services"
 }]
```
