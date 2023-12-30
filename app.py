from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config.pool import lifespan
from src.routes import users

async def exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={'message': 'Internal Server Error'},
    )

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.add_exception_handler(Exception, exception_handler)
