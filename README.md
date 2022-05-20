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
210.214.86.37[IN] Port= 22 TCP
210.214.229.206[IN] Port= 445 TCP
        Vulnerability found= ['CVE-2020-0796']

210.214.170.17[IN] Port= 445 TCP
        Vulnerability found= ['CVE-2020-0796']

210.214.27.8[IN] Port= 135 TCP
210.214.229.106[IN] Port= 139 TCP
210.214.197.229[IN] Port= 23 TCP
210.214.229.43[IN] Port= 445 TCP
        Vulnerability found= ['CVE-2020-0796']
210.214.27.8[IN] Port= 445 TCP
        Vulnerability found= ['CVE-2020-0796']
```

```
Run: python3 shodanScript.py -k "proftpd port:21" 
1.173.112.90[TW] Port= 21 TCP
        Vulnerability found= ['CVE-2010-4652', 'CVE-2009-0543', 'CVE-2009-3639', 'CVE-2008-7265', 'CVE-2011-4130', 'CVE-2010-3867', 'CVE-2012-6095', 'CVE-2011-1137']

37.59.48.108[FR] Port= 21 TCP
        Vulnerability found= ['CVE-2019-12815']

216.218.235.133[US] Port= 21 TCP
195.201.18.77[DE] Port= 21 TCP
        Vulnerability found= ['CVE-2019-12815']
	
203.223.138.247[MY] Port= 21 TCP
98.158.79.204[US] Port= 21 TCP
        Vulnerability found= ['CVE-2015-3306']
	
144.126.135.215[US] Port= 21 TCP
70.32.89.77[US] Port= 21 TCP
2a01:238:432b:4a00:2450:f2fb:249b:3f71[DE] Port= 21 TCP
37.48.111.147[NL] Port= 21 TCP
149.202.147.106[FR] Port= 21 TCP
        Vulnerability found= ['CVE-2015-3306']
```
