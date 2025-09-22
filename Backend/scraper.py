import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

class Scraper:
    def __init__(self):
        self.url_path = "/timetables-and-routes/bus-timetables/"
        self.base_url = "https://www.iombusandrail.im"
        self.url_list = []
        self.pdf_folder = "./tempdata/pdfs/"
        self.image_folder = "./tempdata/images/"

    def scrape(self):
        self.create_pdf_directory()
        self.create_image_directory()
        self.scrape_timetables()
        self.download_files(self.url_list)
        self.convert_pdfs_to_images()

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
            urlretrieve(url, self.pdf_folder + url.split('/')[-1])

    def convert_pdfs_to_images(self):
        for file in os.listdir(self.pdf_folder):
            new_dir = self.image_folder + file.split('.')[0]+ '/'
            self.create_directory(new_dir)
            try:
                convert_from_path(file, dpi=300, output_folder=new_dir)
            except Exception as e:
                print(f"error converting file {file}: {e}")

    def create_directory(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            print(f"error creating directory {path}: {e}")

    def create_pdf_directory(self):
        self.create_directory(self.pdf_folder)

    def create_image_directory(self):
        self.create_directory(self.image_folder)