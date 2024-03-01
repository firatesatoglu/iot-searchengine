from plugins.shodan_search_engine import shodan_search
from plugins.binaryedge_search_engine import binaryedge_search
from plugins.hunterhow_search_engine import hunterhow_search
from plugins.censys_search_engine import censys_search

import pprint
import argparse


#IOT Search Engine Scanner/Crawler/Scraper. 
#This tool is used to search for services on the internet. Easy to search for Shodan, BinaryEdge, HunterHow, Censys
#You need to have API keys for Shodan, BinaryEdge, HunterHow, Censys to use this tool. Set the API keys in the .env file

def main(keyword):
    shodan_search_results= shodan_search(keyword)
    if shodan_search_results != []:
        pprint.pprint(shodan_search_results)

    binaryedge_search_results= binaryedge_search(keyword)
    if binaryedge_search_results != []:
        pprint.pprint(binaryedge_search_results)

    hunterhow_search_results= hunterhow_search(keyword)
    if hunterhow_search_results != []:
        pprint.pprint(hunterhow_search_results)

    # censys_search_results= censys_search(keyword)
    # if censys_search_results != []:
    #     pprint.pprint(censys_search_results)

arguman_parser= argparse.ArgumentParser(description='Search for IoT Services on the internet.')
arguman_parser.add_argument('keyword', type=str, help='Keyword to search for')
args= arguman_parser.parse_args()

if __name__ == "__main__":
    main(args.keyword)