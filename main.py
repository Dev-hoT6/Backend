from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from domain import goods_list, detail, create_review

app = FastAPI()

app.mount('/review_imgs', StaticFiles(directory='review_imgs'), name='review_imgs')

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

app.include_router(goods_list.router)
app.include_router(create_review.router)
app.include_router(detail.router)