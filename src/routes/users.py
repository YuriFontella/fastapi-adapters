from fastapi import APIRouter
from config.pool import pool

router = APIRouter()

@router.get('/users')
async def users():
    async with pool.connection() as conn:
        rows = await conn.execute('SELECT name FROM users LIMIT 1')

    return await rows.fetchone()