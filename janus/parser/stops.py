from janus.ORM.create_record import create_stop
from ORM import schedule_tables as db
import json
import uuid6

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