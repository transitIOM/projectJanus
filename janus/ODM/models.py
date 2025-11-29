from typing import List, Optional
from enum import IntEnum
from datetime import date, time
from bunnet import Document, Link
from pydantic import BaseModel, Field

# --- Enums ---

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
    SIGN = -1
    SHELTER = 0
    STATION = 1

# --- Embedded Models ---

class StopTime(BaseModel):
    """Represents a single stop within a trip. Embedded in Trip."""
    stop_id: str  # Reference to Stop.stop_id
    stop_sequence: int = Field(ge=0)
    arrival_time: time
    departure_time: time
    
    # Metadata
    is_interpolated: bool = False

class CalendarDate(BaseModel):
    """Exception dates for a service. Embedded in Calendar."""
    date: date
    exception_type: ExceptionType

# --- Top-Level Documents (Bunnet) ---

class Agency(Document):
    agency_id: str # GTFS ID
    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_phone: Optional[str] = None
    agency_email: Optional[str] = None
    
    class Settings:
        name = "agencies"

class Calendar(Document):
    """Service availability (calendar.txt)"""
    service_id: str # GTFS ID
    start_date: date
    end_date: date
    
    # Days of week
    monday: DayOption
    tuesday: DayOption
    wednesday: DayOption
    thursday: DayOption
    friday: DayOption
    saturday: DayOption
    sunday: DayOption
    
    # Embedded exceptions (calendar_dates.txt)
    exceptions: List[CalendarDate] = []
    
    class Settings:
        name = "calendars"

class Stop(Document):
    stop_id: str # GTFS ID
    stop_name: str
    stop_lat: float
    stop_lon: float
    wheelchair_boarding: Optional[WheelchairBoarding] = WheelchairBoarding.NO_INFO
    location_type: Optional[LocationType] = LocationType.SHELTER
    
    # Aliases
    aliases: List[str] = []
    
    # Staging / Metadata
    original_scrape_id: Optional[str] = None
    is_ready_for_export: bool = False
    
    class Settings:
        name = "stops"

class Route(Document):
    route_id: str # GTFS ID
    agency_id: Link[Agency] # Reference to Agency document
    route_short_name: str
    route_type: Optional[RouteType] = RouteType.BUS
    route_color: Optional[str] = None
    
    # Staging / Metadata
    scraper_url: Optional[str] = None
    
    class Settings:
        name = "routes"

class Trip(Document):
    trip_id: str # GTFS ID
    route_id: Link[Route]
    service_id: Link[Calendar]
    
    # Embedded Schedule (stop_times.txt)
    stop_times: List[StopTime] = []
    
    # Staging / Metadata
    direction_id: Optional[int] = None
    block_id: Optional[str] = None
    is_ready_for_export: bool = False
    
    class Settings:
        name = "trips"

class Network(Document):
    network_id: str
    route_ids: List[str] = []
    
    class Settings:
        name = "networks"
