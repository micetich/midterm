from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from todo import todo_router  # Assuming 'todo.py' is correctly set up
from file_routes import file_router  # Make sure 'file_routes.py' contains file_router
import os

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def read_index():
    return FileResponse("./frontend/index.html")

# Include routers/this is how I can manage the data from front end to back end

app.include_router(todo_router, prefix="/api")
app.include_router(file_router, prefix="/api")

# Adjust static files serving
app.mount("/MainOpt", StaticFiles(directory="MainOpt"), name="MainOpt")
app.mount("/", StaticFiles(directory="frontend"), name="static")


# Conditional block for development
#if __name__ == "__main__":
   # uvicorn.run(app, host="localhost", port=8000)
