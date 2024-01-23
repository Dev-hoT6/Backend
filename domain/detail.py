from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session


from database import get_db
from models import Product, Review, Cate_1

router = APIRouter(
    prefix="/detail",
)

#
@router.get('/product/{prod_id}')
def get_cate_goods_list(prod_id: str, db:Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id_ == prod_id).first()

    category1 = db.query(Cate_1).filter(Cate_1.id_ == product.cate1).first()

    response_data = {
        "product_name": product.name,
        "product_hashtags": product.hashtag,
        "product_price": product.price,
        "product_image_url": product.img_url,
        "category1": {
            "id": category1.id_,
            "name": category1.name
        }
    }
    return response_data

@router.get('/reviews/{prod_id}')
def get_product_reviews(prod_id:str, db:Session = Depends(get_db)):
    is_product = db.query(Product).where(Product.id_ == prod_id).all()

    if not is_product:
        return HTTPException(status_code=404, detail='no product with the ID')

    reviews = db.query(Review)\
        .where((Review.prod_id == prod_id) & (Review.status == 2))\
        .order_by(Review.id_.desc())\
        .all()

    response_data = {
        'count':len(reviews),
        'product':str(prod_id)
    }

    if reviews:
        response_data['detail'] = [
            {
                 "review_id": review.id_,
                 "review_writer": review.writer,
                 "review_content" : review.content,
                 "review_image_path": review.img_url,
                 "review_points": review.points,
                 "review_status": review.status
            }   for review in reviews
        ]
    else: 
        response_data['detail'] = []

    return response_data