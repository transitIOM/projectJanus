import databases
import orm

database = databases.Database("sqlite:///db.sqlite")
models = orm.ModelRegistry(database=database)

async def startup():
    from . import schedule_tables # noqa: F401 (imported for side effects)
    await database.connect()
    await models.create_all()

async def shutdown():
    await database.disconnect()
