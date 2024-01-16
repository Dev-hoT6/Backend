from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session


from database import get_db
from models import Product, Review, Cate_1, Cate_2

router = APIRouter(
    prefix="/detail",
)

#
@router.get('/product/{prod_id}')
def get_cate_goods_list(prod_id: str, db:Session = Depends(get_db)):
    # with SessionLocal() as db:
    # 상위 카테고리, 하위 카테고리
    # 상품 이름 / 상품 태그 / 상품 가격 / 상품 사진
    # 리뷰 개수 / 리뷰 작성자 / 리뷰 사진
    # 상품 정보 조회
    product = db.query(Product).filter(Product.id_ == prod_id).first()


    # 리뷰 정보 조회
    # reviews = db.query(Review).filter(Review.prod_id == prod_id).all()


    # 카테고리1 정보 조회
    category1 = db.query(Cate_1).filter(Cate_1.id_ == product.cate1).first()
    # 카테고리2 정보 조회
    # category2 = db.query(Cate_2).filter(Cate_2.id_ == product.cate1).first()
    # n_review = len(reviews)

    response_data = {
        "product_name": product.name,
        "product_hashtags": product.hashtag,
        "product_price": product.price,
        "product_image_url": product.img_url,
        "category1_name": category1.name,
        # "n_review": n_review
    }
    return response_data

@router.get('/reviews/{prod_id}')
def get_product_reviews(prod_id:str, db:Session = Depends(get_db)):
        # 리뷰가 있는 경우에만 추가
    #
    reviews = db.query(Review)\
        .where(Review.prod_id == prod_id)\
        .all()

    if reviews:
        response_data = {
            'count':len(reviews),
            'product':str(prod_id),
            'detail': [
                {
                    "review_id": review.id_,
                    "review_writer": review.writer,
                    "review_content" : review.content,
                    "review_image_path": review.img_path,
                    "review_status": review.status
                }   for review in reviews
            ]
        }
    else: 
        response_data = [
            {
                'detail':'no reviews'
            }
        ]
    
    return response_data