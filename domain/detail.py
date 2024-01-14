from fastapi import APIRouter, HTTPException

from database import SessionLocal
from models import Product, Review, Cate_1, Cate_2




router = APIRouter(
    prefix="/detail",
)

#
@router.get('/{ProductId}')
def get_cate_goods_list(ProductId: str):
    with SessionLocal() as db:
        # 상위 카테고리, 하위 카테고리
        # 상품 이름 / 상품 태그 / 상품 가격 / 상품 사진
        # 리뷰 개수 / 리뷰 작성자 / 리뷰 사진
        # 상품 정보 조회
        product = db.query(Product).filter(Product.id_ == ProductId).first()


        # 리뷰 정보 조회
        reviews = db.query(Review).filter(Review.prod_id == ProductId).all()


        # 카테고리1 정보 조회
        category1 = db.query(Cate_1).filter(Cate_1.id_ == product.cate1).first()
        # 카테고리2 정보 조회
        category = db.query(Cate_2).filter(Cate_2.id_ == product.cate1).first()
        n_review = len(reviews)

        response_data = {
            "product_name": product.name,
            "product_hashtags": product.hashtag,
            "product_price": product.price,
            "product_image_url": product.img_url,
            "category1_name": category1.name,
            "n_review": n_review
        }

        # 리뷰가 있는 경우에만 추가
        #
        if reviews:
            response_data["reviews"] = [{
                "review_id": review.id_,
                "review_writer": review.writer,
                "review_content" : review.content,
                "review_image_path": review.img_path,
                "review_status": review.status
            } for review in reviews[:5]]

        return response_data

