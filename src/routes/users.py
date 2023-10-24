from fastapi import APIRouter
from config.pool import database

router = APIRouter()

@router.get('/users')
async def users():
    rows = await database.fetch_one('SELECT name FROM users LIMIT 1')

    return rows
