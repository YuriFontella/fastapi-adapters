import configparser, os
from fastapi import FastAPI

from asyncpg import create_pool
from contextlib import asynccontextmanager

config = configparser.ConfigParser()
config.read('config.ini')

env = os.environ.get('PYTHON_ENV', 'development')

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pool = await create_pool(dsn=config.get(env, 'DSN'), min_size=2, max_size=4)
    yield

    await app.state.pool.close()
