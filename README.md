# IOT Search Engine Scanner/Crawler/Scraper
This tool is used to search for services on the internet. Easy to search for **Shodan**, **BinaryEdge**, **HunterHow**, **Censys**	
	
You need to have API keys for Shodan, BinaryEdge, HunterHow, Censys to use this tool.  **Set the API keys in the .env file**

Usage;

	usage: main.py [-h] keyword
	
	positional arguments:
	  keyword     Keyword to search for
	
	options:
	  -h, --help  show this help message and exit


# Output:

#### example: python3 main.py "http.title:'ID_VC_Welcome' country:'tr'" 

```
{'discovered_date': datetime.datetime(2024, 3, 1, 12, 0, 1, 809978),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['sky<hidden>kom.net'],
                          'ip_address': '18<hidden>4.20',
                          'ip_location': 'TR'},
  'port_info': {'port': '443',
                'product': 'ssh',
                'protocol': 'tcp',
                'vulns': ['CVE-2023-38408',
                          'CVE-2016-20012',
                          'CVE-2018-15919',
                          'CVE-2023-51384',
                          'CVE-2023-51385',
                          'CVE-2019-6111',
                          'CVE-2019-6109']},
  'search_keyword': "http.title:'ID_VC_Welcome' country:'tr'"},

 {'discovered_date': datetime.datetime(2024, 3, 1, 11, 59, 53, 382829),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['ruz<hidden>st.com'],
                          'ip_address': '89<hidden>50',
                          'ip_location': 'TR'},
  'port_info': {'port': '389',
                'product': 'http',
                'protocol': 'tcp',
                'vulns': 'No Vulnerability Found'},
  'search_keyword': "http.title:'ID_VC_Welcome' country:'tr'"},
 {'discovered_date': datetime.datetime(2024, 3, 1, 11, 59, 55, 39271),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['per<hidden>.com',
                                          '<hidden>ting.com.tr'],
                          'ip_address': '213.2<hidden>17',
                          'ip_location': 'TR'},
  'port_info': {'port': '80',
                'product': 'http',
                'protocol': 'tcp',
                'vulns': 'No Vulnerability Found'},
  'search_keyword': "http.title:'ID_VC_Welcome' country:'tr'"},
 {'discovered_date': datetime.datetime(2024, 3, 1, 11, 59, 55, 39276),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['per<hidden>om',
                                          'poyra<hidden>.com.tr'],
                          'ip_address': '213.238<hidden>7',
                          'ip_location': 'TR'},
  'port_info': {'port': '443',
                'product': 'http',
                'protocol': 'tcp',
                'vulns': 'No Vulnerability Found'},
  'search_keyword': "http.title:'ID_VC_Welcome' country:'tr'"},
 {'discovered_date': datetime.datetime(2024, 3, 1, 11, 59, 55, 39277),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['perm<hidden>m',
                                          'p<hidden>m.tr'],
                          'ip_address': '213<hidden>',
                          'ip_location': 'TR'},
  'port_info': {'port': '636',
                'product': 'http',
                'protocol': 'tcp',
                'vulns': 'No Vulnerability Found'},
  'search_keyword': "http.title:'ID_VC_Welcome' country:'tr'"},

 {'discovered_date': datetime.datetime(2024, 3, 1, 11, 59, 55, 39278),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['<hidden>om',
                                          'p<hidden>'],
                          'ip_address': '<hidden>80.117',
                          'ip_location': 'TR'},
  'port_info': {'port': '389',
                'product': 'http',
                'protocol': 'tcp',
                'vulns': 'No Vulnerability Found'},
  'search_keyword': "http.title:'ID_VC_Welcome' country:'tr'"},


 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 30, 446608),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': [],
                          'ip_address': '2606:4700:20::681a:f35',
                          'ip_location': 'US'},
  'port_info': {'port': '443',
                'product': 'http',
                'protocol': 'tcp',
                'vulns': 'No Vulnerability Found'},
  'search_keyword': '<hidden>m.tr'},
  
...
...

No result found for http.title:'ID_VC_Welcome' country:'tr' in BinaryEdge
No result found for http.title:'ID_VC_Welcome' country:'tr' in HunterHow
No result found for http.title:'ID_VC_Welcome' country:'tr' in Censys

```

#### example: python3 main.py hidden.com.tr

```
 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 31, 626496),
  'iot_engine': 'shodan',
  'keyword_information': {'domain_name': ['tirs<hidden>m'],
                          'ip_address': '195.155.137.101',
                          'ip_location': 'TR'},
  'port_info': {'port': '25',
                'product': 'smtp',
                'protocol': 'tcp',
                'vulns': ['CVE-2021-31206']},
  'search_keyword': '<hidden>m.tr'},
  
  
{'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 33, 390519),
  'iot_engine': 'binaryedge',
  'ip_address': '88.255.87.140',
  'port_info': '443',
  'search_keyword': '<hidden>m.tr'},
  
 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 33, 390522),
  'iot_engine': 'binaryedge',
  'ip_address': '88.255.87.140',
  'port_info': '443',
  'search_keyword': '<hidden>m.tr'},
  
                          'ip_address': '104.26.15.53'},
  'port_info': '2082',
  'search_keyword': '<hidden>m.tr'},
 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 36, 299095),
  'iot_engine': 'hunterhow',
  'keyword_information': {'domain_name': 'www.<hidden>m.tr',
                          'ip_address': '104.26.15.53'},
  'port_info': '2086',
  'search_keyword': '<hidden>m.tr'},
 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 36, 299096),
  'iot_engine': 'hunterhow',
  'keyword_information': {'domain_name': '<hidden>m.tr',
                          'ip_address': '104.26.14.53'},
  'port_info': '8080',
  'search_keyword': '<hidden>m.tr'},
  
 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 36, 299097),
  'iot_engine': 'hunterhow',
  'keyword_information': {'domain_name': 'www.<hidden>m.tr',
                          'ip_address': '172.67.70.22'},

 {'discovered_date': datetime.datetime(2024, 3, 1, 12, 7, 36, 299115),
  'iot_engine': 'hunterhow',
  'keyword_information': {'domain_name': 'www.<hidden>m.tr',
                          'ip_address': '104.26.15.53'},
  'port_info': '80',
  'search_keyword': '<hidden>m.tr'}]
```

#iot-search #shodan-search #binaryedge-search #hunterhow-search #searchengine #iotengine #iotenginesearch #icdsearch #icdengine-search
