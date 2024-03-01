from helpers.http_requests import send_get_request
from datetime import datetime 
import json

# Environment Variables
import os 
from pathlib import Path
from dotenv import load_dotenv
enviroment_file_path= Path('./env/.env')
load_dotenv(dotenv_path=enviroment_file_path)

BINARYEDGE_API_URL= os.getenv('BINARYEDGE_API_URL')
BINARYEDGE_API_KEY= os.getenv('BINARYEDGE_API_KEY')
# Environment Variables

def binaryedge_search(search_keyword):
    search_results= []
    binaryedge_search_api= BINARYEDGE_API_URL.format(search_keyword)
    request_status_code, search_request_response= send_get_request(binaryedge_search_api, request_headers={'X-Key': BINARYEDGE_API_KEY}) 

    if request_status_code != 200:
        print(f'Try to get a valid API key from BinaryEdge')
        return search_results
    
    search_response= json.loads(search_request_response.text)
    if search_response['total'] != 0:
        for binaryedge_output in search_response['events']:
            ip_address= binaryedge_output['target']['ip']
            port_information= binaryedge_output['target']['port']

            search_results.append({
                "search_keyword":search_keyword, 
                "ip_address":ip_address, 
                "port_info": str(port_information), 
                "iot_engine": "binaryedge", 
                "discovered_date": datetime.now()
            })
        return search_results
    
    else: print(f'No result found for {search_keyword} in BinaryEdge')
    
