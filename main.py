from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import delete_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    return {"status": "200"}
