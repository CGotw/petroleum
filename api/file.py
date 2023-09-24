from fastapi import APIRouter,File, UploadFile

file_router = APIRouter()


@file_router.get("/file")
async def file(file: UploadFile):
    pass
