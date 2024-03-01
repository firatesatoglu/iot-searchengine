from requests import get, post
import cloudscraper
import time

def send_get_request(request_url, request_headers):
    time.sleep(1) # NOTE: search engines have query rate limit 
    response= get(request_url, headers=request_headers)
    return response.status_code, response

def send_search_request(request_url, post_data):
    request_headers= {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded"}
    response= post(request_url, data=post_data, headers=request_headers)

    return response.status_code, response

def cloudscraper_request(request_url):
    cloudscraper_scraper= cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'windows',
        'mobile': False })

    response= cloudscraper_scraper.get(request_url)
    return response.status_code, response