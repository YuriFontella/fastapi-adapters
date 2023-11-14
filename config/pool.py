import configparser, os

from psycopg_pool import AsyncConnectionPool
from contextlib import asynccontextmanager

config = configparser.ConfigParser()
config.read('config.ini')

env = os.environ.get('PYTHON_ENV', 'development')

pool = AsyncConnectionPool(conninfo=config.get(env, 'CONNINFO'), min_size=2, max_size=4)

@asynccontextmanager
async def lifespan(app):
    await pool.wait()
    yield

    await pool.close()