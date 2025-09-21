import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.url_path = "/timetables-and-routes/bus-timetables/"
        self.base_url = "https://www.iombusandrail.im"

    def scrape_timetables(self):

        reqs = requests.get(self.base_url + self.url_path)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.pdf'):
                urls.append(self.base_url + href)
        return urls