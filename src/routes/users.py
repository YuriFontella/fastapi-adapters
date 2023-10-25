from fastapi import APIRouter, Request
from asyncpg import Pool

router = APIRouter()

@router.get('/users')
async def users(request: Request):
    pool: Pool = request.app.state.pool
    async with pool.acquire() as conn:
        rows = await conn.fetch('SELECT name FROM users LIMIT 1')

    return rows