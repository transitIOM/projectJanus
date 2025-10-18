from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from pdf2image import convert_from_path

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
            text = link.text
            if href and href.endswith('.pdf'):
                self.url_list.append((self.base_url + href, text))
        return self.url_list

    def download_files(self, urls):
        url_list = [x[0] for x in urls]
        for url in url_list:
            urlretrieve(url, self.pdf_folder + url.split('/')[-1])

    def process_file(self, file, create_directory):
        new_dir = os.path.join(self.image_folder, file.split('.')[0])
        create_directory(new_dir)
        try:
            convert_from_path(
                os.path.join(self.pdf_folder, file),
                output_folder=new_dir,
                dpi=300,
                fmt='png',
                output_file='page'
            )
            return file, None
        except Exception as e:
            return file, e

    def convert_pdfs_to_images(self):
        files = os.listdir(self.pdf_folder)
        total = len(files)
        done = 0

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(
                    self.process_file,
                    file,
                    self.create_directory
                ): file
                for file in files
            }

            for future in as_completed(futures):
                file, err = future.result()
                done += 1
                if err:
                    print(f"[{done}/{total}] error converting {file}: {err}")
                else:
                    print(f"[{done}/{total}] finished {file}")

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