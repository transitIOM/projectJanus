from .database import models
import orm
import datetime
import enum

# info about orm types --> https://www.encode.io/typesystem/fields/
# gtfs schedule reference --> https://gtfs.org/documentation/schedule/reference/

class Timetables(orm.Model):
    tablename = "timetables"
    registry = models
    fields = {
        "timetable_name": orm.String(primary_key=True, max_length=None),
        "hash": orm.String(max_length=None),
        "conversion_date": orm.Date(default=datetime.date.today())
    }

class Agency(orm.Model):
    tablename = "agency"
    registry = models
    fields = {
        "agency_id": orm.String(primary_key=True, max_length=None),
        "agency_name": orm.String(max_length=None),
        "agency_url": orm.URL(max_length=None),
        "agency_timezone": orm.String(max_length=None),
        "agency_phone": orm.String(max_length=None),
        "agency_email": orm.Email(max_length=None),
    }

class DayEnum(enum.Enum):
    _0 = "avalible for all of day in date range"
    _1 = "not avalible for all of day in date range"

class Calendar(orm.Model):
    tablename = "calendar"
    registry = models
    fields = {
        "service_id": orm.String(primary_key=True, max_length=None),
        "start_date": orm.Date(),
        "end_date": orm.Date(),
        "monday": orm.Enum(DayEnum, default=DayEnum._1),
        "tuesday": orm.Enum(DayEnum, default=DayEnum._1),
        "wednesday": orm.Enum(DayEnum, default=DayEnum._1),
        "thursday": orm.Enum(DayEnum, default=DayEnum._1),
        "friday": orm.Enum(DayEnum, default=DayEnum._1),
        "saturday": orm.Enum(DayEnum, default=DayEnum._1),
        "sunday": orm.Enum(DayEnum, default=DayEnum._1),
    }

class ExceptionTypeEnum(enum.Enum):
    _1 = "service has been added for the specified date"
    _2 = "service has been removed for the specified date"

class CalendarDates(orm.Model):
    tablename = "calendar_dates"
    registry = models
    fields = {
        "service_id": orm.ForeignKey(Calendar),
        "date": orm.Date(primary_key=True),
        "exception_type": orm.Enum(ExceptionTypeEnum),
    }

class WheelchairBoardingEnum(enum.Enum):
    _0 = "no accessibility information for the stop"
    _1 = "some vehicles at this stop can be boarded by a rider in a wheelchair"
    _2 = "wheelchair boarding is not possible at this stop"

class Stops(orm.Model):
    tablename = "stops"
    registry = models
    fields = {
        "stop_id": orm.String(primary_key=True, max_length=None), # peenus - tom
        "stop_name": orm.String(unique=True, max_length=None),
        "stop_lat": orm.Decimal(allow_null=True, max_digits=23, decimal_places=20),
        "stop_long": orm.Decimal(allow_null=True, max_digits=23, decimal_places=20),
        "wheelchair_boarding": orm.Enum(WheelchairBoardingEnum, default=WheelchairBoardingEnum._0)
    }

class StopNameAlias(orm.Model):
    tablename = "StopNameAlias"
    registry = models
    fields = {
        "stop_name": orm.ForeignKey(Stops),
        "alias": orm.String(primary_key=True, max_length=None),
    }

class RouteTypeEnum(enum.Enum):
    _0 = "tram, streetcar, light rail. any light rail or street level system within a metropolitan area"
    _1 = "subway, metro. any underground rail system within a metropolitan area"
    _2 = "rail. used for intercity or long-distance travel"
    _3 = "bus. used for short- and long-distance bus routes"
    _4 = "ferry. used for short- and long-distance boat service"
    _5 = "cable tram. used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in san francisco)"
    _6 = "aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables"
    _7 = "funicular. any rail system designed for steep inclines"
    _11 = "trolleybus. electric buses that draw power from overhead wires using poles"
    _12 = "monorail. railway in which the track consists of a single rail or a beam"

class Routes(orm.Model):
    tablename = "routes"
    registry = models
    fields = {
        "route_id": orm.String(primary_key=True, max_length=None),
        "agency_id": orm.String(allow_blank=True, coerce_types=True, max_length=None),
        "route_short_name": orm.String(max_length=12),
        "route_type": orm.Enum(RouteTypeEnum, default=RouteTypeEnum._3),
        "route_color": orm.String(max_length=6),
        "timetable_name": orm.ForeignKey(Timetables),
    }

class Trips(orm.Model):
    tablename = "trips"
    registry = models
    fields = {
        "trip_id": orm.String(primary_key=True, max_length=None),
        "route_id": orm.ForeignKey(Routes),
        "service_id": orm.ForeignKey(Calendar),
        "timetable_name": orm.ForeignKey(Timetables),
    }

class StopTimes(orm.Model):
    tablename = "stop_times"
    registry = models
    fields = {
        "trip_id": orm.ForeignKey(Trips),
        "stop_id": orm.ForeignKey(Stops),
        "stop_sequence": orm.Integer(primary_key=True, minimum=0),
        "arrival_time": orm.Time(),
        "departure_time": orm.Time(),
        "timetable_name": orm.ForeignKey(Timetables),
    }

class Networks(orm.Model):
    tablename = "networks"
    registry = models
    fields = {
        "network_id": orm.String(primary_key=True, max_length=None),
    }

class RouteNetworks(orm.Model):
    tablename = "route_networks"
    registry = models
    fields = {
        "network_id": orm.ForeignKey(Networks, primary_key=True),
        "route_id": orm.ForeignKey(Routes, primary_key=True),
    }