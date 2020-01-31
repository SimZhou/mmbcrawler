from bs4 import BeautifulSoup
import requests
import re


def get_price(url):
    h = get_html(url)
    price_raw = h.find('form', action='price.aspx').find_next_sibling().find('script', type="text/javascript").text
    price = re.findall(r"chart\(.*?\);", price_raw)[0].strip('chart(').strip(');')
    return price

def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    return soup



