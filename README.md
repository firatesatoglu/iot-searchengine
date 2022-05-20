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
210.214.170.52[IN] Port= 445 TCP 
        Vulnerability found= ['CVE-2020-0796']

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

210.214.186.32[IN] Port= 135 TCP
210.214.62.186[IN] Port= 22 TCP
210.214.27.8[IN] Port= 445 TCP
        Vulnerability found= ['CVE-2020-0796']
```
