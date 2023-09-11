from fastapi import APIRouter

file_router = APIRouter()


@file_router.get("/file")
async def file():
    mysql=g
