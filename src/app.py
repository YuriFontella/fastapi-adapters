from fastapi import FastAPI, Depends
from asyncpg import Pool

from config.pool import lifespan

import src.routes.users

app = FastAPI(lifespan=lifespan)

app.include_router(src.routes.users.router)