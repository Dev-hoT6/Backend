from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import pickle
import numpy as np

from .review_schema import ReviewCreate

from database import get_db
from models import Review, Product, Vectors, Cate_1

from neural_networks.vectorizer import sbert
from neural_networks.binarizer import *

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
    # 방금 생성된 리뷰의 ID 반환
    return str(db.query(Review.id_).order_by(Review.id_.desc()).first()[0])

def create_vector(rev_id, vec, db: Session):
    db_vector = Vectors(id_=rev_id,
                        vector=vec)
    db.add(db_vector)
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
    # prod_id = str(prod_id)

    # 상품 리뷰의 카테고리 가져오기
    cateid = db.query(Product.cate1).where(Product.id_ == prod_id).first()[0]
    category = db.query(Cate_1.name).where(Cate_1.id_ == cateid).first()[0]
    
    # 리뷰 DB에 저장, 리뷰 ID 반환
    rev_id = create_review(prod_id, db, review_create)
    
    # 생성된 카테고리와 리뷰 모델에 넣어서 벡터 가져오기
    vector = sbert([category, review_create.content]) 
    # print(vector)

    # binary_vector = pickle.dumps(vector)
    binary_vector = vector
    
    create_vector(rev_id, binary_vector, db)
    
    return {
        'id' : rev_id,
        'vector' : str(vector.tolist())
    }

@router.post('/submit/{rev_id}', status_code=status.HTTP_201_CREATED)
def get_review_point(rev_id:str, db: Session = Depends(get_db)):
    ## 리뷰 등록 가능 신호를 받고 
    ## Input: 리뷰 ID
    ## Output: REVIEW 테이블의 Point 컬럼에 적립 포인트 저장

    ## Response: 등록 성공 코드(201)

    vec = db.query(Vectors.vector).where(Vectors.id_ == str(rev_id)).first()[0]

    return {'vector':rev_id}