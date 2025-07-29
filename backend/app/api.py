from dotenv import load_dotenv
from fastapi import FastAPI

from backend.app.database import engine, Base
from backend.app.routes import user_router

load_dotenv()
app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(user_router.router, prefix="/users", tags=["user"])