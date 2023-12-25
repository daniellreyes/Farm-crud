from pydantic import BaseModel

class Task:
    id: str
    title: str
    description: str
    completed: bool = False