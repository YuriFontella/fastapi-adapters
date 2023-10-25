import configparser, os

from databases import Database
from contextlib import asynccontextmanager

config = configparser.ConfigParser()
config.read('config.ini')

env = os.environ.get('PYTHON_ENV', 'development')
    
database = Database(url=config.get(env, 'URL'), min_size=2, max_size=4)

@asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield

    await database.disconnect()
