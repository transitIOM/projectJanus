from Backend.src.ORM.create_record import create_stop
from ORM.schedule_tables import *
import json

class Stops:
    async def get_existing_stops():
        return await Stops.objects.all()

    def get_stops_from_file(filePath):
        with open(filePath, 'r') as file:
            data = json.load(file)

        bus_stops = []
        for table in data['tables']:
            rows = table['rows']

        for row in rows:
            if row[0] == "Place":
                next
            bus_stop_name = row[0]
            bus_stops.append(bus_stop_name)
        return bus_stops