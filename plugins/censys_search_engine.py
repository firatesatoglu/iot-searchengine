from helpers.http_requests import cloudscraper_request
from datetime import datetime 
from bs4 import BeautifulSoup

# Environment Variables
import os 
from pathlib import Path
from dotenv import load_dotenv
enviroment_file_path= Path('./env/.env')
load_dotenv(dotenv_path=enviroment_file_path)

CENSYS_API_URL= os.getenv('CENSYS_API_URL')
# Environment Variables# # 

def censys_search(domain):
    search_results= []
    search_query= CENSYS_API_URL.format(domain)
    
    request_status_code, censys_search_response= cloudscraper_request(search_query)
    if request_status_code != 200:
        print(f'error in Censys')
        return search_results
    
    else:
        censys_html_content= BeautifulSoup(censys_search_response.content, 'html.parser')
        for censys_output in censys_html_content.find_all('div', ['SearchResult result']):
            ip_address= censys_output.find('strong').get_text()
            port_info= censys_output.find('div', ['services-results']).get_text().strip()
            all_found_ports= port_info.replace('\n\n', ',').split(' ')
            for found_port in all_found_ports:
                if found_port != '':
                    search_results.append({
                        "domain_name":domain, 
                        "ip_address":ip_address, 
                        "port_info":str(found_port), 
                        "iot_engine": "censys", 
                        "discovered_date": datetime.now()
                    })
        
        return search_results
