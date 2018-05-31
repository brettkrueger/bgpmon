# bgpmon

[![Build Status](https://travis-ci.org/MustyMouse/bgpmon.svg?branch=master)](https://travis-ci.org/MustyMouse/bgpmon)  

A Python wrapper for the bgpmon (https://bgpmon.net) SOAP API.  

### How to install
```
pip install bgpmon
```
or
```
git clone https://github.com/zksnarky/bgpmon.git
cd bgpmon
python setup.py build
python setup.py install
```
### Example usage
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
### Example usage with proxy
```
>>> from bgpmon import *
>>> bgpmon=BGPMon('http://user:password@host:port')
>>> print(bgpmon.getIpInfo(email,passwd,"103.201.129.0"))
[(Prefix_info){
   prefix = "103.201.129.0/24"
   prefix_description = "xTom Japan"
   country_code = "unknown"
   origin_as = "134829"
   origin_as_name = "xTom Global Anycast Services"
 }]
```
