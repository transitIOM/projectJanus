from pymongo import MongoClient
from bunnet import init_bunnet

try:
    from .models import Agency, Calendar, Stop, Route, Trip, Network
except ImportError:
    from models import Agency, Calendar, Stop, Route, Trip, Network

def init_mongo(connection_string: str = "mongodb://localhost:27017", db_name: str = "janus_gtfs"):
    # Initialize the synchronous MongoDB connection and Bunnet ODM.
    client = MongoClient(connection_string)
    
    # Initialize Bunnet with the document models
    init_bunnet(
        database=client[db_name],
        document_models=[
            Agency,
            Calendar,
            Stop,
            Route,
            Trip,
            Network
        ]
    )
    print(f"Successfully connected to MongoDB ({db_name}) and initialized Bunnet models.")

if __name__ == "__main__":
    init_mongo()
