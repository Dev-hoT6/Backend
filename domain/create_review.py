from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .review_schema import ReviewCreate

from database import get_db
from models import Review

from neural_networks.vectorizer import vectorize

router = APIRouter(
    prefix="/review/create",
)


### CRUD
def create_review(prod_id, db: Session, review: ReviewCreate):
    db_review = Review(prod_id=prod_id,
                       writer=review.writer,
                       img_url=review.img_url,
                       content=review.content)
    db.add(db_review)
    db.commit()
    

### Router
@router.post('/{prod_id}', status_code=status.HTTP_200_OK)
def get_new_review_send_vector(prod_id:str,
                               review_create:ReviewCreate,
                               db: Session = Depends(get_db)):
    ## 리뷰를 받아서 서버의 DB에 저장.
    ## Input: 카테고리ID(str), 리뷰 본문(str), 리뷰 이미지(img)
    ## Output: 1. REVIEW 테이블에 리뷰 본문, 이미지저장
    ##         2. VECTORS 테이블에 리뷰 ID와 카테고리, 리뷰 벡터(Binary) 저장

    ## Response: 리뷰 ID(str), 리뷰 벡터(str)
    prod_id = str(prod_id)
    create_review(prod_id, db, review_create)

    vector = str(vectorize().tolist()) ### 모델을 넣어서 벡터 가져오기

    return {
        'id' : prod_id,
        'vector' : vector
    }

@router.post('/submit/{review_id}', status_code=status.HTTP_201_CREATED)
def get_review_point(db: Session = Depends(get_db)):
    ## 리뷰 등록 가능 신호를 받고 
    ## Input: 카테고리ID(str), 리뷰 본문(str)
    ## Output: REVIEW 테이블의 Point 컬럼에 적립 포인트 저장

    ## Response: 등록 성공 코드(201), 리뷰 코드



    return {
        'review_id': '000'
    }