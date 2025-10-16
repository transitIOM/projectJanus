import databases
import orm
import datetime

database = databases.Database("sqlite:///db.sqlite")
models = orm.ModelRegistry(database=database)

# info about orm types --> https://www.encode.io/typesystem/fields/
# gtfs schedule reference --> https://gtfs.org/documentation/schedule/reference/



class timetables(orm.Model):
    tablename = "timetables"
    registry = models
    fields = {
        "hash": orm.String(primary_key=True),
        "timetable_name": orm.String(),
        "conversion_date": orm.Date(default=datetime.date.today())
    }

class calendar(orm.Model):
    tablename = "calendar"
    registry = models
    fields = {
        "service_id": orm.String(primary_key=True),
        "start_date": orm.Date(),
        "end_date": orm.Date(),
        "monday": orm.Enum((1,0), ("service is available for all Mondays in the date range", "service is not available for Mondays in the date range")),
        "tuesday": orm.Enum((1,0), ("service is available for all tuesdays in the date range", "service is not available for tuesdays in the date range")),
        "wednesday": orm.Enum((1,0), ("service is available for all wednesdays in the date range", "service is not available for wednesdays in the date range")),
        "thursday": orm.Enum((1,0), ("service is available for all thursdays in the date range", "service is not available for thursdays in the date range")),
        "friday": orm.Enum((1,0), ("service is available for all fridays in the date range", "service is not available for fridays in the date range")),
        "saturday": orm.Enum((1,0), ("service is available for all saturdays in the date range", "service is not available for saturdays in the date range")),
        "sunday": orm.Enum((1,0), ("service is available for all sundays in the date range", "service is not available for sundays in the date range")),
    }

class calendar_dates(orm.Model):
    tablename = "calendar_dates"
    registry = models
    fields = {
        "service_id": orm.ForeignKey(calendar, primary_key=True),
        "date": orm.Date(primary_key=True),
        "exception_type": orm.Enum((1,2),("service has been added for the specified date", "service has been removed for the specified date")),
    }

class stops(orm.Model):
    tablename = "stops"
    registry = models
    fields = {
        "stop_id": orm.String(primary_key=True),
        "stop_name": orm.String(),
        "stop_lat": orm.Decimal(allow_null=True),
        "stop_long": orm.Decimal(allow_null=True),
        "wheelchair_boarding": orm.Enum((0,1,2),("no accessibility information for the stop", "some vehicles at this stop can be boarded by a rider in a wheelchair", "wheelchair boarding is not possible at this stop"), default=0)
    }

class routes(orm.Model):
    tablename = "routes"
    registry = models
    fields = {
        "route_id": orm.String(primary_key=True),
        "agency_id": orm.String(allow_blank=True, coerce_types=True),
        "route_short_name": orm.String(max_length=12),
        "route_type": orm.Enum(
            (0, 1, 2, 3, 4, 5, 6, 7, 11, 12),
            (   "tram, streetcar, light rail. any light rail or street level system within a metropolitan area",
                "subway, metro. any underground rail system within a metropolitan area",
                "rail. used for intercity or long-distance travel",
                "bus. used for short- and long-distance bus routes",
                "ferry. used for short- and long-distance boat service",
                "cable tram. used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in san francisco)",
                "aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables",
                "funicular. any rail system designed for steep inclines",
                "trolleybus. electric buses that draw power from overhead wires using poles",
                "monorail. railway in which the track consists of a single rail or a beam"),
        default=3),
        "route_color": orm.String(max_length=6),
    }

class trips(orm.Model):
    tablename = "trips"
    registry = models
    fields = {
        "trip_id": orm.String(primary_key=True),
        "route_id": orm.ForeignKey(routes),
        "service_id": orm.ForeignKey(calendar),
    }

class stop_times(orm.Model):
    tablename = "stop_times"
    registry = models
    fields = {
        "trip_id": orm.ForeignKey(trips, primary_key=True),
        "stop_id": orm.ForeignKey(stops),
        "stop_sequence": orm.Integer(primary_key=True, minimum=0),
        "arrival_time": orm.Time(),
        "departure_time": orm.Time(),
    }

class networks(orm.Model):
    tablename = "networks"
    registry = models
    fields = {
        "network_id": orm.String(primary_key=True),
    }

class route_networks(orm.Model):
    tablename = "route_networks"
    registry = models
    fields = {
        "network_id": orm.ForeignKey(networks, primary_key=True),
        "route_id": orm.ForeignKey(routes, primary_key=True),
    }