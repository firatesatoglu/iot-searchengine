from helpers.http_requests import send_get_request
from datetime import datetime 
import json

# Environment Variables
import os 
from pathlib import Path
from dotenv import load_dotenv
enviroment_file_path= Path('./env/.env')
load_dotenv(dotenv_path=enviroment_file_path)

SHODAN_SEARCH_URL=  os.getenv('SHODAN_SEARCH_URL')
SHODAN_HOST_URL= os.getenv('SHODAN_HOST_URL')
SHODAN_API_KEY= os.getenv('SHODAN_API_KEY')
# Environment Variables

def shodan_search(search_keyword):
    search_results= []
    shodan_search_api= SHODAN_SEARCH_URL.format(search_keyword, SHODAN_API_KEY)
    shodan_host_api= SHODAN_HOST_URL

    request_status_code, shodan_search_response = send_get_request(shodan_search_api, {})
    if request_status_code != 200:
        print(f'Try to get a valid API key from Shodan')
        return search_results
    
    shodan_search_response_json = json.loads(shodan_search_response.text)
    if shodan_search_response_json['total'] != 0:
        for shodan_output in shodan_search_response_json['matches']:
            ip_address= shodan_output['ip_str']
            ip_location= shodan_output['location']['country_code']
            domain_name= shodan_output['domains']

            request_status_code, host_information_request= send_get_request(shodan_host_api.format(ip_address, SHODAN_API_KEY), {})
            host_information= json.loads(host_information_request.text)
            host_all_ports= host_information['ports']
            for host_port in host_all_ports:
                results_data= {
                        "search_keyword":search_keyword, 
                        "keyword_information": {
                                "ip_address": ip_address, 
                                "ip_location": ip_location, 
                                "domain_name": domain_name
                            },
                        "port_info": {
                            "port": str(host_port), 
                            "protocol": host_information['data'][0]['transport'],
                            "product": host_information['data'][0]['_shodan']['module'],
                            "vulns": host_information['vulns'] if 'vulns' in host_information else "No Vulnerability Found",
                        },
                        "iot_engine": "shodan",
                        "discovered_date": datetime.now()
                    }
                
                search_results.append(results_data)
                # print(results_data)
    
        return search_results
    
    else: print(f'No result found for {search_keyword} in Shodan')