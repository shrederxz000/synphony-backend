from typing import Annotated, Optional
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel, Field
import uvicorn


app = FastAPI()

class CreateUser(BaseModel):
    name:Annotated[str, Field(min_length=1, max_length=50)] | None = None
    email:EmailStr
    age:Annotated[int, Field(ge=18, le=120)]


@app.get('/')
def index():
    return {'msg':'hello'}

@app.get('/hello')
def hello(name:str = 'world'):
    name = name.strip().title()
    return {'msg': f'hello {name}'}

@app.post('/users')
def create_user(user:CreateUser):
    return {
        'message': 'ok',
        'name': user.name,
        'email': user.email,
        'age': user.age
}





if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)
