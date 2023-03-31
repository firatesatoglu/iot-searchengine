censysAPIEndpoint= """https://search.censys.io/_search?resource=hosts&per_page=100&virtual_hosts=EXCLUDE&q={0}"""
shodanSearchAPI= """https://api.shodan.io/shodan/host/search?key={0}&query={1}"""
shodanhHostAPI= """https://api.shodan.io/shodan/host/{1}?key={0}"""
APIKEY= ''

from bs4 import BeautifulSoup
import cloudscraper
import argparse
import requests 
import json
import time

def main(keyword):
    shodanSearch(keyword)
    censysSearch(keyword)

def sendRequest(apiEndpoint, searchKeyword):
    time.sleep(2)
    requestforSearch = requests.get(apiEndpoint.format(APIKEY, searchKeyword)).content.decode('utf-8')
    jsonResponse= json.loads(requestforSearch)
    return jsonResponse

def shodanSearch(keyword):
    print('Shodan', '-'*40, 'Shodan')
    for shodanOutput in sendRequest(shodanSearchAPI, keyword)['matches']:
        ipAddress= shodanOutput['ip_str']
        shodanURL= f"https://www.shodan.io/host/{ipAddress}"
        ipLocation= shodanOutput['location']['country_code']
        domaninName= shodanOutput['domains']
        
        try:
            hostInfo= sendRequest(shodanhHostAPI, ipAddress)
            portInfo= hostInfo['ports']
            vulnerabiltyInfo= f"Vulnerabilty Info: {hostInfo.get('vulns')}" if hostInfo.get('vulns') else ''
            organizationInfo= hostInfo['org']
            print(f'IP Address: {ipAddress} [{ipLocation}]\n SHODAN URL: {shodanURL}\n Ports are Open: {portInfo}\n Domain Info: {domaninName}, {organizationInfo}\n {vulnerabiltyInfo}\n')
        except:
            pass

def censysSearch(keyword):
    if ':' in keyword:
        keyword= keyword.split(':')[1].replace("'", '').replace('"', '').strip()

    cloudFlare = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False}, interpreter='nodejs')
    
    print('Censys', '-'*40, 'Censys')
    time.sleep(10)
    cloudflareRequest= cloudFlare.get(censysAPIEndpoint.format(keyword))
    parseContent = BeautifulSoup(cloudflareRequest.content, 'html.parser')
    for censysOutput in parseContent.find_all('div', ['SearchResult result']):
        ipAddress= censysOutput.find('strong').get_text()
        portInfo= censysOutput.find('div', ['services-results']).get_text().strip()
        print(f"IP Address: {ipAddress}\n Ports are Open: {portInfo.split()}\n")

def readFile(filePath):
    with open(filePath, 'r+', encoding='utf-8') as dorkList:
        dorkList= dorkList.readlines()
        for dorks in dorkList:
            main(dorks.strip())

argParse = argparse.ArgumentParser(description='Shodan Script make doing something')
argParse.add_argument('-k','--keyword', help='Just give keyword, Dork and it search for you')
argParse.add_argument('-f','--file', help='Just give wordlist, dork list')
# argParse.add_argument('-o','--output', help='Redirect Output! \'Defualt write current directory\'')

parseArgument= vars(argParse.parse_args())
userKeyword= parseArgument['keyword']
userFile= parseArgument['file']
# userOutput= parseArgument['output']

if __name__ == '__main__':
    if APIKEY == '':
        print('Please change APIKEY variable in script')
        exit()

    if bool(userKeyword)== True:
        main(userKeyword)
    if bool(userFile)== True:
        readFile(userFile)
