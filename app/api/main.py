import time

from pydantic import BaseModel
from fastapi import Request, FastAPI, APIRouter, HTTPException


app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"request processed in {process_time} s")
    return response


class Request(BaseModel):
    username: str
    password: str

class Response(BaseModel):
    username: str
    email: str

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/employee/{id}", response_model=Response)
def employee(id: int):
    if id == 4:
        raise HTTPException(status_code=400, detail="No user with that id")
    return {"username": "johndoe", "email": "abc@gmail.com"}

@app.post("/login")
async def login(req: Request):
    if req.username == "user1" and req.password == "password":
        return {"message": "success"}
    return {"message": "Authentication Failed"}


v2 = APIRouter()

@v2.get("/test")
def home2():
    return {"Hello": "World"}


app.include_router(v2, prefix="/v2")