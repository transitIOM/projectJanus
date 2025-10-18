from src.parser.stops import get_stops_from_file

path = "output.json"
output = get_stops_from_file(path)

print(output)