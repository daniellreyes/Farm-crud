from fastapi import FastAPI
from database import get_all_tasks, create_task
from models import Task

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI API'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks

@app.post('/api/tasks')
async def create_task(task: Task):
    print(task)
    return 'create task'

@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'

@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'updating tasks'

@app.delete('/api/tasks/{id}')
async def delete_task():
    return 'delete task'

