from loguru import logger
from pymongo import MongoClient
from bunnet import init_bunnet
from pymongo.errors import ConnectionFailure

try:
    from .models import Agency, Calendar, Stop, Route, Trip, Network, StopTime, CalendarDate
except ImportError:
    from models import Agency, Calendar, Stop, Route, Trip, Network, StopTime, CalendarDate

def init_mongo(connection_string: str = "mongodb://localhost:27017", db_name: str = "janus_gtfs"):
    # Initialize the synchronous MongoDB connection and Bunnet ODM.
    try:
        client = MongoClient(connection_string)
    except ConnectionFailure:
        logger.error("Could not connect to MongoDB")
        quit()

    # Initialize Bunnet with the document models
    init_bunnet(
        database=client[db_name],
        document_models=[
            Agency,
            Calendar,
            CalendarDate,
            Stop,
            Route,
            StopTime,
            Trip,
            Network,
        ]
    )
    print(f"Successfully connected to MongoDB ({db_name}) and initialized Bunnet models.")

if __name__ == "__main__":
    init_mongo()
