from fastapi import APIRouter, Request

router = APIRouter()

@router.get('/users')
async def users(request: Request):
    pool = request.app.state.pool
    async with pool.acquire() as conn:
        rows = await conn.fetch('SELECT name FROM users LIMIT 1')

    return rows