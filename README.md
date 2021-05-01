# Shodan Search Script
Shodan script for easy search on Shodan.

First by first you need CHANGE API KEY, with your API key in code. 

Usage;

	python3 shodanScript.py -f dorkList.txt -o output.txt
	python3 shodanScript.py -k "net:'210.214.0.0/16'" -o output.txt
	
-h, --help  show this help message and exit

	-k  Just give keyword, Dork and it search for you
	-w  Just give wordlist, dork list
 
