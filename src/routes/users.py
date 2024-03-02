from fastapi import APIRouter
from config.pool import database

router = APIRouter()

@router.get('/users')
async def users():
    async with database.transaction():
        return await database.fetch_one('SELECT name FROM users LIMIT 1')
