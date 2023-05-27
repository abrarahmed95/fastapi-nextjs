from typing import Union

from fastapi import FastAPI, APIRouter

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app = FastAPI()
app.include_router(router)