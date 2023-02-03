# Shodan Search Script
Shodan script for easy search on Shodan.

First by first you need CHANGE API KEY, with your API key in code. 

Usage;

	python3 shodanScript.py -f dorkList.txt
	python3 shodanScript.py -k "net:'210.214.0.0/16'"
	python3 shodanScript.py -k "http.title:'ID_VC_Welcome' country:'tr'" 
	
-h, --help  show this help message and exit

	-k  Just give keyword, Dork and it search for you
	-w  Just give wordlist, dork list
 
Output:

```
Run: python3 shodanScript.py -k "net:'210.214.0.0/16'"

Shodan ------------------------------------------------------------ Shodan
IP Address: 210.214.170.239 [IN]
 Ports are Open: [161, 515, 137, 9002, 587, 80, 443]
 Domain Info: ['sify.net'], Sify Limited
 
IP Address: 210.214.142.238 [IN]
 Ports are Open: [135, 137, 445, 80, 1434, 49679, 3389]
 Domain Info: ['sify.net'], Sify Limited
 Vulnerabilty Info: ['CVE-2020-0796']

IP Address: 210.214.27.26 [IN]
 Ports are Open: [5357, 445, 135]
 Domain Info: ['sify.net'], Sify Limited
 Vulnerabilty Info: ['CVE-2020-0796']

Censys ------------------------------------------------------------ Censys
IP Address: 210.214.2.170
 Ports are Open: ['22/SSH', '23/TELNET']

IP Address: 210.214.6.22
 Ports are Open: ['23/TELNET', '80/HTTP', '443/HTTP', '541/UNKNOWN']

IP Address: 210.214.7.146
 Ports are Open: ['80/HTTP', '123/NTP', '443/HTTP']

IP Address: 210.214.7.150
 Ports are Open: ['22/SSH', '23/TELNET', '69/TFTP', '80/HTTP', '137/NETBIOS', '443/UNKNOWN']

```

```
Run: python3 shodanScript.py -k "proftpd port:21" 
Shodan ------------------------------------------------------------ Shodan

IP Address: 18.195.36.254 [DE]
 Ports are Open: [80, 443, 21]
 Domain Info: ['amazonaws.com'], A100 ROW GmbH
 Vulnerabilty Info: ['CVE-2019-19271', 'CVE-2021-46854', 'CVE-2019-19272', 'CVE-2020-9272', 'CVE-2019-19269']

IP Address: 185.175.202.189 [NL]
 Ports are Open: [993, 995, 587, 110, 143, 80, 21, 22, 25, 443]
 Domain Info: ['axc.eu'], CLDIN B.V.
 Vulnerabilty Info: ['CVE-2018-20685', 'CVE-2017-15906', 'CVE-2021-36368', 'CVE-2020-14145', 'CVE-2018-15473', 'CVE-2020-15778', 'CVE-2021-41617', 'CVE-2018-15919', 'CVE-2016-20012', 'CVE-2019-6110', 'CVE-2019-6111', 'CVE-2019-6109']

IP Address: 2a03:f480:1:c::72 [EE]
 Ports are Open: [993, 995, 3306, 587, 80, 465, 21, 22, 443]
 Domain Info: ['playback.ru'], IPv6 network for hosting services
 Vulnerabilty Info: ['CVE-2019-19271', 'CVE-2019-19272', 'CVE-2018-15919', 'CVE-2017-15906', 'CVE-2021-36368', 'CVE-2022-37451', 'CVE-2019-19269', 'CVE-2018-15473', 'CVE-2020-14145', 'CVE-2020-15778', 'CVE-2020-9272', 'CVE-2021-41617', 'CVE-2022-37452', 'CVE-2021-46854', 'CVE-2018-20685', 'CVE-2016-20012', 'CVE-2019-6110', 'CVE-2019-6111', 'CVE-2019-6109']

IP Address: 153.122.13.148 [JP]
 Ports are Open: [993, 995, 110, 143, 8880, 465, 21, 22, 25, 123, 53]
 Domain Info: ['cleanmat-sys.jp'], DIX Co., Ltd.
 Vulnerabilty Info: ['CVE-2019-19271', 'CVE-2019-19272', 'CVE-2019-19269', 'CVE-2020-9272', 'CVE-2021-46854', 'CVE-2019-12815']

IP Address: 200.145.78.19 [BR]
 Ports are Open: [2000, 8008, 80, 8020, 21, 443]
 Domain Info: ['unesp.br'], UNIVERSIDADE ESTADUAL PAULISTA
 

IP Address: 50.205.55.168 [US]
 Ports are Open: [993, 995, 587, 8880, 465, 21, 8443, 25, 443, 53]
 Domain Info: ['smartgate.com'], Comcast Cable Communications, LLC

IP Address: 2a01:4f8:173:27a6::2 [DE]
 Ports are Open: [993, 123, 587, 80, 465, 995, 21, 4949, 443, 10000, 53]
 Domain Info: ['studioeleven.gr'], Stefanis I. Nicolaos
 Vulnerabilty Info: ['CVE-2019-0220', 'CVE-2017-7679', 'CVE-2020-1934', 'CVE-2014-3581', 'CVE-2016-0736', 'CVE-2014-3583', 'CVE-2015-3185', 'CVE-2015-3184', 'CVE-2015-3183', 'CVE-2018-1312', 'CVE-2020-35452', 'CVE-2017-9798', 'CVE-2022-22720', 'CVE-2022-28330', 'CVE-2019-10092', 'CVE-2016-8612', 'CVE-2019-0217', 'CVE-2022-22721', 'CVE-2006-20001', 'CVE-2017-15710', 'CVE-2013-5704', 'CVE-2019-17567', 'CVE-2017-15715', 'CVE-2022-31813', 'CVE-2016-2161', 'CVE-2019-10098', 'CVE-2015-3306', 'CVE-2016-5387', 'CVE-2021-40438', 'CVE-2022-30556', 'CVE-2022-23943', 'CVE-2020-1927', 'CVE-2018-17199', 'CVE-2017-9788', 'CVE-2014-8109', 'CVE-2018-1301', 'CVE-2018-1302', 'CVE-2018-1303', 'CVE-2017-3167', 'CVE-2021-34798', 'CVE-2017-3169', 'CVE-2020-11985', 'CVE-2015-0228', 'CVE-2021-44790', 'CVE-2022-37436', 'CVE-2021-26690', 'CVE-2021-26691', 'CVE-2022-26377', 'CVE-2016-4975', 'CVE-2020-13938', 'CVE-2018-1283', 'CVE-2022-29404', 'CVE-2016-8743', 'CVE-2021-44224', 'CVE-2022-22719', 'CVE-2022-28615', 'CVE-2022-28614', 'CVE-2022-36760', 'CVE-2021-39275']

IP Address: 209.50.61.44 [US]
 Ports are Open: [10000, 80, 21, 22, 3000, 443]
 Domain Info: ['upcloud.host'], UpCloud USA San Jose

------------------------------------------------------------ Censys

IP Address: 1.0.0.1
 Ports are Open: ['53/DNS', '80/HTTP', '443/HTTP', '853/UNKNOWN', '2052/HTTP', '2053/UNKNOWN', '2082/HTTP', '2083/UNKNOWN', '2086/HTTP', '2087/UNKNOWN', '2095/HTTP', '2096/UNKNOWN', '8080/HTTP', '8443/UNKNOWN', '8880/HTTP']

IP Address: 1.0.0.4
 Ports are Open: ['80/HTTP', '443/HTTP', '2052/HTTP', '2053/HTTP', '2082/HTTP', '2083/HTTP', '2086/HTTP', '2087/HTTP', '2095/HTTP', '2096/HTTP', '8080/HTTP', '8443/HTTP', '8880/HTTP']

IP Address: 1.0.0.6
 Ports are Open: ['80/HTTP', '443/HTTP', '2052/HTTP', '2053/HTTP', '2082/HTTP', '2083/HTTP', '2086/HTTP', '2087/HTTP', '2095/HTTP', '2096/HTTP', '8080/HTTP', '8443/HTTP', '8880/HTTP']
```
