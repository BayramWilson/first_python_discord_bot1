import requests
from bs4 import BeautifulSoup as bs

def fetch_latest_news_title():
    URL = 'https://tarnkappe.info/newsticker'
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    section = soup.find('section')
    if section:
        first_ul = section.find('ul')
        first_link = first_ul.find('a')

        if first_link:
            title = first_link.text.strip()
            link = first_link['href']
            return title
        
def fetch_latest_news_link():
    URL = 'https://tarnkappe.info/newsticker'
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')
    section = soup.find('section')
    if section:
        first_ul = section.find('ul')
        first_link = first_ul.find('a')

        if first_link:
            title = first_link.text.strip()
            link = first_link['href']
            return link
        

# print(fetch_latest_news_title())
# print(fetch_latest_news_link())