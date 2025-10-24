from database import db
from entities import DayOptions, ExceptionTypeOptions, WheelchairBoardingOptions, RouteTypeOptions, LocationTypeOptions
from pony.orm import *

def build_all_enums():
    build_day_options()
    build_exception_type_options()
    build_wheelchair_boarding_options()
    build_route_type_options()
    build_location_type_options()

@db_session
def build_day_options():
    #TODO check if entries
    #TODO change to use new class structure
    _0 = DayOptions(value=0, description="avalible for all of day in date range")
    _1 = DayOptions(value=1, description="not avalible for all of day in date range")

@db_session
def build_exception_type_options():
    _1 = ExceptionTypeOptions(value=1, description="service has been added for the specified date")
    _2 = ExceptionTypeOptions(value=2, description="service has been removed for the specified date")

@db_session
def build_wheelchair_boarding_options():
    _0 = WheelchairBoardingOptions(value=0, description="no accessibility information for the stop")
    _1 = WheelchairBoardingOptions(value=1, description="some vehicles at this stop can be boarded by a rider in a wheelchair")
    _2 = WheelchairBoardingOptions(value=2, description="wheelchair boarding is not possible at this stop")

@db_session
def build_route_type_options():
    _0 = RouteTypeOptions(value=0, description="tram, streetcar, light rail. any light rail or street level system within a metropolitan area")
    _1 = RouteTypeOptions(value=1, description="subway, metro. any underground rail system within a metropolitan area")
    _2 = RouteTypeOptions(value=2, description="rail. used for intercity or long-distance travel")
    _3 = RouteTypeOptions(value=3, description="bus. used for short- and long-distance bus routes")
    _4 = RouteTypeOptions(value=4, description="ferry. used for short- and long-distance boat service")
    _5 = RouteTypeOptions(value=5, description="cable tram. used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in san francisco)")
    _6 = RouteTypeOptions(value=6, description="aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables")
    _7 = RouteTypeOptions(value=7, description="funicular. any rail system designed for steep inclines")
    _11 = RouteTypeOptions(value=11, description="trolleybus. electric buses that draw power from overhead wires using poles")
    _12 = RouteTypeOptions(value=12, description="monorail. railway in which the track consists of a single rail or a beam")

@db_session
def build_location_type_options():
    _-1 = LocationTypeOptions(value=-1, description="just a sign")
    _0 = LocationTypeOptions(value=0, description="a proper bus shelter")
    _1 = LocationTypeOptions(value=1, description="idk smth like lord street")