from janus.ORM import entities as db
from rapidfuzz import fuzz
from rapidfuzz import process
import json
import uuid6
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

class Stops:
    def __init__(self):
        self.file_stops = []
        
    def get_stops_from_file(self, filePath):
        self.file_stops = []
        with open(filePath, 'r') as file:
            data = json.load(file)

        for table in data['tables']:
            rows = table['rows']

        for row in rows:
            if row[0] == "Place":
                next
            bus_stop_name = row[0]
            self.file_stops.append(bus_stop_name)
    
    async def check_for_new(self, name) -> str:
        try:
            exists = await db.Stops.objects.filter(stop_name__iexact=name).exists()
        except Exception as e:
            print(e)
            return "db query failed"

        if exists == False:
            try:
                await create_stop(uuid6.uuid7(), name)
            except Exception as e:
                print(e)
                return("failed creating stop entry")
            return "created new stop entry"
        
        return "stop exists"
    
    def is_match(self, name1, name2):
        match = fuzz.token_sort_ratio(name1, name2)
        if match >= 75:
            return True
        
        return False
    
class busTimesScraper:
    def get_routes():
        bus_vannin_routes_page = "https://bustimes.org/operators/bus-vannin"
        reqs = requests.get(bus_vannin_routes_page)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        for route in soup.find_all():
            short = route.text()
            url = route.parent.parent.get("href")
            print(short, url)