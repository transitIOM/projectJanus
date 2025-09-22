import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve

class Scraper:
    def __init__(self):
        self.url_path = "/timetables-and-routes/bus-timetables/"
        self.base_url = "https://www.iombusandrail.im"
        self.url_list = []

    def scrape(self):
        self.create_pdf_directory()
        self.create_image_directory()
        self.scrape_timetables()
        self.download_files(self.url_list)

    def scrape_timetables(self):
        reqs = requests.get(self.base_url + self.url_path)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.pdf'):
                self.url_list.append(self.base_url + href)
        return self.url_list

    def download_files(self, urls):
        for url in urls:
            urlretrieve(url, "./data/pdfs/" + url.split('/')[-1])

    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            print(f"Error creating directory {path}: {e}")

    def create_pdf_directory(self):
        self.create_directory("./data/pdfs")

    def create_image_directory(self):
        self.create_directory("./data/images")