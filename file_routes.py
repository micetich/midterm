from fastapi import APIRouter
import os
from fastapi.responses import JSONResponse

file_router = APIRouter()

@file_router.get("/list-cmd-reg-files")
async def list_cmd_reg_files():
    directory = 'MainOpt'
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('.bat', '.cmd', '.reg'))]
    return JSONResponse(content={"files": files})
