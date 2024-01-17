from pydantic import BaseModel


class ReviewCreate(BaseModel):
    writer: str
    content: str

class Review(BaseModel):
    prod_id: str
    writer: str
    content: str
    points: int
    status: int
