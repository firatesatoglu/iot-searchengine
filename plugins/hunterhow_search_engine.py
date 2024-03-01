from helpers.http_requests import send_get_request
from datetime import datetime 
import base64
import json

# Environment Variables
import os 
from pathlib import Path
from dotenv import load_dotenv
enviroment_file_path= Path('./env/.env')
load_dotenv(dotenv_path=enviroment_file_path)

HUNTERHOW_API_URL= os.getenv('HUNTERHOW_API_URL')
HUNTERHOW_API_KEY= os.getenv('HUNTERHOW_API_KEY')
# Environment Variables

def hunterhow_search(search_keyword):
    search_results= []
    encoded_keyword= base64.urlsafe_b64encode(f'domain="{search_keyword}"'.encode("utf-8")).decode('ascii')
    hunterhow_search_api= HUNTERHOW_API_URL.format(encoded_keyword, HUNTERHOW_API_KEY)
    request_status_code, hunterhow_search_response = send_get_request(hunterhow_search_api, request_headers={'X-Api-Key': HUNTERHOW_API_KEY}) 

    hunterhow_search_response_json = json.loads(hunterhow_search_response.text)
    if hunterhow_search_response_json['code'] == 200: 
        for hunterhow_output in hunterhow_search_response_json['data']['list']:
            ip_address= hunterhow_output['ip']
            domain_name= hunterhow_output['domain']
            port_info= hunterhow_output['port']
            search_results.append({
                "search_keyword":search_keyword, 
                "keyword_information": {"ip_address": ip_address, "domain_name": domain_name},
                "port_info": str(port_info), 
                "iot_engine": "hunterhow", 
                "discovered_date": datetime.now()
            })

        return search_results
    
    elif hunterhow_search_response_json['code'] == 401:
        print(f'Try to get a valid API key from HunterHow')
        return search_results
    
    else:
        print(f'No result found for {search_keyword} in HunterHow')