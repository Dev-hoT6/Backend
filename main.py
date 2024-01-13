from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import SessionLocal
from models import Product

app = FastAPI()


origins = [
    "http://localhost:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/hello")
def hello():
    return {"message": "hello world"}


