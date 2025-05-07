from fastapi import FastAPI

app = FastAPI()


@app.get('/root')
def root():
    return {'message': 'hello'}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", reload=True)
