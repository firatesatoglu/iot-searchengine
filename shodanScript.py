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
def shodanSearch(searchKeyword, outputFile):
    try:
        print('🔥')
        apiforSearch= "https://api.shodan.io/shodan/host/search?"
        GuthmaerAPI= '******************************' #API_KEY !!!CHANGE ME
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
                result= f'{ipAddr}[{locationCountryCode}] Port= {ipPort} {dataProtocol} \n\tVulnerability found= {list(iter(allVuln))}\n'
                writeFile(result, outputFile)
            except KeyError: 
                result= f'{ipAddr}[{locationCountryCode}] Port= {ipPort} {dataProtocol}'
                writeFile(result, outputFile)
                pass
    except Exception:
        print('I cant find anything :/')

def writeFile(searchResult, outputFile):
    if os.path.exists(outputFile)== True:
        with open(outputFile,'r+', encoding='utf-8') as result:
            bacResult= result.read()
            result.seek(0)
            result.write(searchResult+'\n'+bacResult)
    else:
        createFile=open(outputFile,'w', encoding='utf-8')
        with open(outputFile,'r+', encoding='utf-8') as result:
            bacResult= result.read()
            result.seek(0)
            result.write(searchResult+'\n'+bacResult)

def readFile(fileInput, outputFile):
    if os.path.exists(outputFile)== True:
        with open(fileInput, 'r+', encoding='utf-8') as dorkList:
            alldork= dorkList.readlines()
            for dork in alldork:
                shodanSearch(dork, outputFile)
    else:
        print('Where is the file?')
        
def keywordSearch(keywordInput, outputFile):
    shodanSearch(keywordInput, outputFile)

argParse = argparse.ArgumentParser(description='Shodan Script make doing something')
argParse.add_argument('-k','--keyword', help='Anahtar kelimeye göre arama')
argParse.add_argument('-f','--file', help='Kelime listesine göre arama ')
argParse.add_argument('-o','--output', help='Çıktıyı bir yere yönlendir \'Varsayılan olarak bulunduğun dizine yeni bir dosya oluşturur\'')

parseArgument= vars(argParse.parse_args())
userKeyword= parseArgument['keyword']
userFile= parseArgument['file']
userOutput= parseArgument['output']

if bool(userKeyword)== True:
    if bool(userOutput)== True:
        keywordSearch(userKeyword, userOutput)
    else:
        userOutput= 'shodanOutput.txt'
        keywordSearch(userKeyword, userOutput)

if bool(userFile)== True:
    if bool(userOutput)== True:
        readFile(userFile, userOutput)
    else:
        userOutput= 'shodanOutput.txt'
        shodanSearch(userFile, userOutput)
