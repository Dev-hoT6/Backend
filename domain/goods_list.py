from fastapi import APIRouter

from database import SessionLocal
from models import Product, Cate_1, Cate_2

router = APIRouter(
    prefix="/product",
)


@router.get('/')
def get_goods_list():
    with SessionLocal() as db:
        # goods_list = db.query(Product).all()

        goods_list = db.query(Product.id_, Product.name, Product.price, Product.img_url).all()
        cate_list = db.query(Cate_1.name).all()
    n_goods = len(goods_list)
    cate_list = [x[0] for x in cate_list]
    return {
        'n_goods' : n_goods,
        'category' : cate_list,
        'goods' : [{'id':i, 'name': n, 'price':p, 'img_url':u} for i, n, p, u in goods_list]
    }


# @router.get('/categories/{}')
# def get_cate_goods_list():
#     return {
#         'id' : '68155',
#         'cate' : '01'
#     }