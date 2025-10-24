from pony.orm import *
from database import db
from entities import *
from build_enums import build_all_enums

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
build_all_enums()