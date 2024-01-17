from pydantic import BaseModel, field_validator


class ReviewCreate(BaseModel):
    prod_id: str
    writer: str
    content: str

    # @field_validator('content')
    # def not_empty(cls, v):
    #     if not v or not v.strip():
    #         raise ValueError('빈 값은 허용되지 않습니다.')
    #     return v

class Review(BaseModel):
    prod_id: str
    writer: str
    content: str
    points: int
    status: int
