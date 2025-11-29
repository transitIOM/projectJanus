from typing import List, Optional
from enum import IntEnum
from datetime import date, time
from bunnet import Document, Link, Indexed
from pydantic import BaseModel, Field
import pymongo


class DayOption(IntEnum):
    TRUE = 0
    FALSE = 1

class ExceptionType(IntEnum):
    ADDED = 1
    REMOVED = 2

class WheelchairBoarding(IntEnum):
    NO_INFO = 0
    POSSIBLE = 1
    NOT_POSSIBLE = 2

class RouteType(IntEnum):
    TRAM = 0
    SUBWAY = 1
    RAIL = 2
    BUS = 3
    FERRY = 4
    CABLE_TRAM = 5
    AERIAL_LIFT = 6
    FUNICULAR = 7
    TROLLEYBUS = 11
    MONORAIL = 12

class LocationType(IntEnum):
    STOP = 0
    STATION = 1
    ENTRANCE_EXIT = 2
    GENERIC_NODE = 3
    BOARDING_AREA = 4


class Agency(Document):
    agency_id: Indexed(str, index_type=pymongo.TEXT, unique=True) # GTFS ID
    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_phone: Optional[str] = None
    agency_email: Optional[str] = None
    
    class Settings:
        name = "agencies"

class Calendar(Document):
    """Service availability (calendar.txt)"""
    service_id: Indexed(str, index_type=pymongo.TEXT, unique=True) # GTFS ID
    start_date: date
    end_date: date
    
    # Days of the week
    monday: DayOption
    tuesday: DayOption
    wednesday: DayOption
    thursday: DayOption
    friday: DayOption
    saturday: DayOption
    sunday: DayOption
    
    class Settings:
        name = "calendars"

class CalendarDate(Document):
    """Exception dates for a service. (calendar_dates.txt)"""
    service_id: Link[Calendar] # Reference to Calendar.service_id
    date: date
    exception_type: ExceptionType

    class Settings:
        name = "calendar_dates"

class StopName(BaseModel):
    name: str
    source: str
    primary: bool = False

class Stop(Document):
    stop_id: Indexed(str, index_type=pymongo.TEXT, unique=True) # GTFS ID
    stop_names: List[StopName]
    stop_lat: float
    stop_lon: float
    wheelchair_boarding: Optional[WheelchairBoarding] = WheelchairBoarding.NO_INFO
    location_type: Optional[LocationType] = LocationType.STOP
    
    # Staging / Metadata
    original_scrape_id: Optional[str] = None
    is_ready_for_export: bool = False
    
    class Settings:
        name = "stops"
        indexes = [
            "stop_names.name",
        ]

class Route(Document):
    route_id: Indexed(str, index_type=pymongo.TEXT, unique=True) # GTFS ID
    agency_id: Link[Agency] # Reference to an Agency document
    route_short_name: str
    route_type: Optional[RouteType] = RouteType.BUS
    route_color: Optional[str] = None
    route_long_name: Optional[str] = None
    route_url: Optional[str] = None
    
    # Staging / Metadata
    scraper_url: Optional[str] = None
    
    class Settings:
        name = "routes"

class StopTime(Document):
    """Represents a single stop within a trip. (stop_times.txt)"""
    stop_id: Link[Stop]  # Reference to Stop.stop_id
    stop_sequence: int = Field(ge=0)
    arrival_time: time
    departure_time: time

    # Metadata
    is_interpolated: bool = False

    class Settings:
        name = "stop_times"

class Trip(Document):
    trip_id: Indexed(str, index_type=pymongo.TEXT, unique=True) # GTFS ID
    route_id: Link[Route]
    service_id: Link[Calendar]
    trip_headsign: Optional[str] = None
    shape_id: Optional[str] = None
    
    # Embedded Schedule (stop_times.txt)
    stop_times: List[StopTime] = []
    
    # Staging / Metadata
    direction_id: Optional[int] = None
    block_id: Optional[str] = None
    is_ready_for_export: bool = False
    
    class Settings:
        name = "trips"

class Network(Document):
    network_id: Indexed(str, index_type=pymongo.TEXT, unique=True)
    route_ids: List[str] = []
    
    class Settings:
        name = "networks"
