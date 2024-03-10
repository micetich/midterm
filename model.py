from pydantic import BaseModel

class TodoRequest(BaseModel):
    title: str
    description: str

class Todo(TodoRequest):
    id: int

def model_dump(self):
    return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
