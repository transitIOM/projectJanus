from .schedule_tables import *
from typing import Optional
from decimal import Decimal
import datetime

async def create_timetable(
    timetable_name: str,
    hash: str,
    conversion_date: Optional[datetime.date]
) -> Timetables:
    """
    create a new timetable entry
    
    args:
        hash: unique hash identifier for the timetable
        timetable_name: human-readable name of the timetable
        conversion_date: date when the timetable was converted (defaults to today)
    
    returns:
        the created timetables instance
    """
    timetable = await Timetables.objects.create(
        hash=hash,
        timetable_name=timetable_name,
        conversion_date=conversion_date or datetime.date.today()
    )
    return timetable

async def create_agency(
    agency_id: str,
    agency_name: str,
    agency_url: str,
    agency_timezone: str,
    agency_phone: str,
    agency_email: str
) -> Agency:
    """
    create a new agency entry
    
    args:
        agency_id: unique identifier for the transit agency
        agency_name: full name of the transit agency
        agency_url: url of the transit agency's website
        agency_timezone: timezone where the transit agency is located
        agency_phone: phone number for the transit agency
        agency_email: email address for the transit agency
    
    returns:
        the created agency instance
    """
    agency = await Agency.objects.create(
        agency_id=agency_id,
        agency_name=agency_name,
        agency_url=agency_url,
        agency_timezone=agency_timezone,
        agency_phone=agency_phone,
        agency_email=agency_email
    )
    return agency

async def create_calendar(
    service_id: str,
    start_date: datetime.date,
    end_date: datetime.date,
    monday: int,
    tuesday: int,
    wednesday: int,
    thursday: int,
    friday: int,
    saturday: int,
    sunday: int
) -> Calendar:
    """
    create a new calendar service entry
    
    args:
        service_id: unique identifier for the service schedule
        start_date: start date of the service period
        end_date: end date of the service period
        monday: service available on mondays (1=yes, 0=no)
        tuesday: service available on tuesdays (1=yes, 0=no)
        wednesday: service available on wednesdays (1=yes, 0=no)
        thursday: service available on thursdays (1=yes, 0=no)
        friday: service available on fridays (1=yes, 0=no)
        saturday: service available on saturdays (1=yes, 0=no)
        sunday: service available on sundays (1=yes, 0=no)
    
    returns:
        the created calendar instance
    """
    calendar = await Calendar.objects.create(
        service_id=service_id,
        start_date=start_date,
        end_date=end_date,
        monday=monday,
        tuesday=tuesday,
        wednesday=wednesday,
        thursday=thursday,
        friday=friday,
        saturday=saturday,
        sunday=sunday
    )
    return calendar

async def create_calendar_date(
    service_id: str,
    date: datetime.date,
    exception_type: int
) -> CalendarDates:
    """
    create a new calendar date exception
    
    args:
        service_id: identifier for the service schedule
        date: particular date for the service exception
        exception_type: type of exception (1=service added, 2=service removed)
    
    returns:
        the created calendardates instance
    """
    calendar_date = await CalendarDates.objects.create(
        service_id=service_id,
        date=date,
        exception_type=exception_type
    )
    return calendar_date

async def create_stop(
    stop_id: str,
    stop_name: str,
    stop_lat: Optional[Decimal] = None,
    stop_long: Optional[Decimal] = None,
    wheelchair_boarding: int = 0
) -> Stops:
    """
    create a new stop entry
    
    args:
        stop_id: unique identifier for the stop
        stop_name: name of the stop
        stop_lat: latitude of the stop location (optional)
        stop_long: longitude of the stop location (optional)
        wheelchair_boarding: wheelchair accessibility (0=no info, 1=accessible, 2=not accessible)
    
    returns:
        the created stops instance
    """
    stop = await Stops.objects.create(
        stop_id=stop_id,
        stop_name=stop_name,
        stop_lat=stop_lat,
        stop_long=stop_long,
        wheelchair_boarding=wheelchair_boarding
    )
    return stop

async def create_route(
    route_id: str,
    agency_id: str,
    route_short_name: str,
    route_type: int,
    route_color: str,
    timetable_name: str,
) -> Routes:
    """
    create a new route entry
    args:
        route_id: unique identifier for the route
        agency_id: identifier for the agency operating this route
        route_short_name: short public-facing name for the route
        route_type: type of transportation (0=tram, 1=subway, 2=rail, 3=bus, etc)
        route_color: color designation for the route (hex code or color name)
        timetable_name: identifier for the timetable associated with this route
        
    returns:
        the created routes instance
    """
    route = await Routes.objects.create(
        route_id=route_id,
        agency_id=agency_id,
        route_short_name=route_short_name,
        route_type=route_type,
        route_color=route_color,
        timetable_name=timetable_name,
    )
    return route

async def create_trip(
    trip_id: str,
    route_id: str,
    service_id: str,
    timetable_name: str,
) -> Trips:
    """
    create a new trip entry
    
    args:
        trip_id: unique identifier for the trip
        route_id: identifier for the route this trip belongs to
        service_id: identifier for the service schedule this trip follows
        timetable_name: identifier for the timetable associated with this route
    
    returns:
        the created trips instance
    """
    trip = await Trips.objects.create(
        trip_id=trip_id,
        route_id=route_id,
        service_id=service_id,
        timetable_name=timetable_name,
    )
    return trip

async def create_stop_time(
    trip_id: str,
    stop_id: str,
    stop_sequence: int,
    arrival_time: datetime.time,
    departure_time: datetime.time,
    timetable_name: str,
) -> StopTimes:
    """
    create a new stop time entry
    
    args:
        trip_id: identifier for the trip
        stop_id: identifier for the stop
        stop_sequence: order of stops for this trip (starting from 0 or 1)
        arrival_time: arrival time at the stop
        departure_time: departure time from the stop
        timetable_name: identifier for the timetable associated with this route
    
    returns:
        the created stoptimes instance
    """
    stop_time = await StopTimes.objects.create(
        trip_id=trip_id,
        stop_id=stop_id,
        stop_sequence=stop_sequence,
        arrival_time=arrival_time,
        departure_time=departure_time
    )
    return stop_time

async def create_network(
    network_id: str
) -> Networks:
    """
    create a new network entry
    
    args:
        network_id: unique identifier for the network
    
    returns:
        the created networks instance
    """
    network = await Networks.objects.create(
        network_id=network_id
    )
    return network

async def create_route_network(
    network_id: str,
    route_id: str
) -> RouteNetworks:
    """
    create a new route-network association
    
    args:
        network_id: identifier for the network
        route_id: identifier for the route to associate with the network
    
    returns:
        the created routenetworks instance
    """
    route_network = await RouteNetworks.objects.create(
        network_id=network_id,
        route_id=route_id
    )
    return route_network