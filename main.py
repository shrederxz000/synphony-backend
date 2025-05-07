from fastapi import FastAPI
import uvicorn

from items.views import router as items_router
from users.views import router as users_router


app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def index():
    return {"msg": "hello"}


@app.get("/hello")
def hello(name: str = "world"):
    name = name.strip().title()
    return {"msg": f"hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
