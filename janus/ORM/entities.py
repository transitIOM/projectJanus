from pony.orm import *
from database import db
import datetime

# info about orm types --> https://www.encode.io/typesystem/fields/
# gtfs schedule reference --> https://gtfs.org/documentation/schedule/reference/

class Timetables(db.Entity):
    timetable_name = Set(lambda: Trips)
    hash = Required(str, unique=True)
    conversion_date = Optional(datetime.date, default=datetime.date.today)

class Agency(db.Entity):
    agency_id = Set(lambda: Routes)
    agency_name = Required(str)
    agency_url = Required(str)
    agency_timezone = Required(str)
    agency_phone = Optional(str)
    agency_email = Optional(str)

class DayOptions(db.Entity):
    value = Required(int)
    description = Required(str)

class Calendar(db.Entity):
    service_id = Set(lambda: CalendarDates)
    trips = Set(lambda: Trips)
    start_Date = Required(datetime.date)
    end_date = Required(datetime.date)
    monday = Required(int)
    tuesday = Required(int)
    wednesday = Required(int)
    thursday = Required(int)
    friday = Required(int)
    saturday = Required(int)
    sunday = Required(int)

class ExceptionTypeOptions(db.Entity):
    value = Required(int)
    description = Required(str)

class CalendarDates(db.Entity):
    service_id = Required(Calendar)
    date = Required(datetime.date)
    exception_type = Required(int, min=1, max=2)
    PrimaryKey(service_id, date)

class WheelchairBoardingOptions(db.Entity):
    value = Set(lambda: Stops)
    description = Required(str)

class LocationTypeOptions():
    value = Set(lambda: Stops)
    description = Required(str)

class Stops(db.Entity):
    stop_id = Set(lambda: StopTimes) # peenus - tom
    stop_name = Set(lambda: StopNameAlias)
    stop_lat = Required(float)
    stop_long = Required(float)
    wheelchair_boarding = Optional(WheelchairBoardingOptions, default=0)
    location_type = Optional(LocationTypeOptions, default=0)

class StopNameAlias(db.Entity):
    stop_name = Required(Stops)
    alias = Required(str)
    PrimaryKey(stop_name, alias)

class RouteTypeOptions(db.Entity):
    value = Set(lambda: Routes)
    description = Required(str)

class Routes(db.Entity):
    route_id = Set(lambda: Trips)
    agency_id = Required(Agency)
    route_short_name = Required(str, 12)
    route_type = Optional(RouteTypeOptions, default=3)
    route_color = Optional(str, 6)

class Trips(db.Entity):
    trip_id = Set(lambda: StopTimes)
    route_id = Required(Routes)
    service_id = Required(Calendar)
    timetable_id = Required(Timetables)

class StopTimes(db.Entity):
    trip_id = Required(Trips)
    stop_id = Required(Stops)
    stop_sequence = Required(int, min=0)
    arrival_time = Required(datetime.time)
    departure_time = Required(datetime.time)

class Networks(db.Entity):
    network_id = Set(lambda: RouteNetworks)

class RouteNetworks(db.Entity):
    network_id = Required(Networks)
    route_id = Required(str)
    PrimaryKey(network_id, route_id)