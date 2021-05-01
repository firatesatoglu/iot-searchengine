import requests 
import json
import argparse
import os
#import time 
#from bs4 import BeautifulSoup 
 
#headers = { 
#         'User-Agent': 
#         ("**************************************************************************************************************")}#Linux 
#proxy = { 
#    "https": '**********************', 
#    "http": '**********************' } 
#justCookie= {'cf_clearance': '***********************************************************'}

#class myAuth(requests.auth.AuthBase):
#    def __call__(self, requ):
#        requests.get('https://account.shodan.io/login', headers=headers, auth=('Guthmaer', '**********************'))
#        return requ

#Author: Guthmaer
def shodanSearch(searchKeyword):
    try:
        print("Wait...")
        apiforSearch= "https://api.shodan.io/shodan/host/search?"
        GuthmaerAPI= '**********************************' #API_KEY !!!CHANGE ME
        searchQuery= apiforSearch + "key=" + GuthmaerAPI + '&query=' + searchKeyword

        requestforSearch = requests.get(searchQuery)  #headers=headers, proxies=proxy, cookies=justCookie
        contentbySearch= requestforSearch.content.decode('utf-8')
        searchJson= json.loads(contentbySearch)
    
        for fromShodan in searchJson['matches']:
            ipAddr= fromShodan['ip_str'] #or host
            ipPort= fromShodan['port']
            dataProtocol= fromShodan['transport'].upper() #TCP or UDP
            location= fromShodan['location'] #'country_name', 'country_code', 'city' 
            locationCountryName= location['country_name'] 
            locationCountryCode= location['country_code'] 
            locationCountryCity= location['city'] 
            
            try: 
                allVuln = fromShodan['vulns'] 
                print(f'{ipAddr}[{locationCountryCode}] Port= {ipPort} {dataProtocol} \n\tVulnerability found= {list(iter(allVuln))}\n')
            except KeyError: 
                print(f'{ipAddr}[{locationCountryCode}] Port= {ipPort} {dataProtocol}')
                pass
    except Exception:
        print('I cant find anything :/')

# def writeFile(searchResult, outputFile):
#     if os.path.exists(outputFile)== True:
#         with open(outputFile,'r+', encoding='utf-8') as result:
#             bacResult= result.read()
#             result.seek(0)
#             result.write(searchResult+'\n'+bacResult)
#     else:
#         createFile=open(outputFile,'w', encoding='utf-8')
#         with open(outputFile,'r+', encoding='utf-8') as result:
#             bacResult= result.read()
#             result.seek(0)
#             result.write(searchResult+'\n'+bacResult)

def readFile(fileInput):
    if os.path.exists(fileInput)== True:
        with open(fileInput, 'r+', encoding='utf-8') as dorkList:
            alldork= dorkList.readlines()
            for dork in alldork:
                shodanSearch(dork)
    else:
        print('Where is the file?')
        
argParse = argparse.ArgumentParser(description='Shodan Script make doing something')
argParse.add_argument('-k','--keyword', help='Just give keyword, Dork and it search for you')
argParse.add_argument('-f','--file', help='Just give wordlist, dork list')
# argParse.add_argument('-o','--output', help='Redirect Output! \'Defualt write current directory\'')

parseArgument= vars(argParse.parse_args())
userKeyword= parseArgument['keyword']
userFile= parseArgument['file']
# userOutput= parseArgument['output']

if bool(userKeyword)== True:
    shodanSearch(userKeyword)

if bool(userFile)== True:
    readFile(userFile)
