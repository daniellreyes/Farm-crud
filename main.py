from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI API'}

@app.get('/api/tasks')
async def get_tasks():
    return 'all tasks'

@app.post('/api/tasks')
async def create_tasks():
    return 'create tasks'

@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'

@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'updating tasks'

@app.delete('/api/tasks/{id}')
async def delete_task():
    return 'delete task'

