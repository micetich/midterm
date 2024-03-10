from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoRequest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from file_routes import file_router
todo_router = APIRouter()

todo_list = []
max_id: int = 0

@todo_router.post("/todos", status_code=status.HTTP_201_CREATED, response_model=Todo)
async def add_todo(todo: TodoRequest) -> JSONResponse:
    global max_id
    max_id += 1  # auto increment ID
    new_todo = Todo(id=max_id, **todo.dict())
    todo_list.append(new_todo)
    return JSONResponse(content=jsonable_encoder(new_todo), status_code=status.HTTP_201_CREATED)

@todo_router.get("/todos", response_model=list[Todo])
async def get_todos() -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(todo_list))

@todo_router.get("/todos/{id}", response_model=Todo)
async def get_todo_by_id(id: int = Path(..., title="The ID of the todo to get")) -> JSONResponse:
    for todo in todo_list:
        if todo.id == id:
            return JSONResponse(content=jsonable_encoder(todo))
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with ID={id} not found.")

@todo_router.put("/todos/{id}", response_model=Todo)
async def update_todo(id: int, todo_request: TodoRequest) -> JSONResponse:
    for todo in todo_list:
        if todo.id == id:
            todo.title = todo_request.title
            todo.description = todo_request.description
            return JSONResponse(content=jsonable_encoder(todo))
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with ID={id} not found.")

@todo_router.delete("/todos/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int) -> JSONResponse:
    for i, todo in enumerate(todo_list):
        if todo.id == id:
            del todo_list[i]
            return {"message": f"Todo with ID={id} has been deleted."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with ID={id} not found.")

