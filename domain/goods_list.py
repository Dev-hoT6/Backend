from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Product, Cate_1




router = APIRouter(
    prefix="/product",
)

### CRUD
def get_goods_list(db: Session = Depends(get_db)):
    goods_list = db.query(Product.id_, Product.name, Product.price, Product.img_url).all()
    cate_list = db.query(Cate_1.id_, Cate_1.name).all()
    return goods_list, cate_list

def get_cate_goods_list(CateId: str, db: Session = Depends(get_db)):
    result = db.query(Product.id_, Product.name, Product.price, Product.img_url, Cate_1.name)\
            .join(Cate_1, Product.cate1 == Cate_1.id_)\
            .where(Product.cate1 == CateId).all()
    return result



### Router
@router.get('/')
def goods_list(db: Session = Depends(get_db)):
    goods_list, cate_list = get_goods_list(db)
    n_goods = len(goods_list)

    return {
        'n_goods' : n_goods,
        'category' : [{'id':i, 'name': n} for i, n in cate_list],
        'goods' : [{'id':i, 'name': n, 'price':p, 'img_url':u} for i, n, p, u in goods_list]
    }


@router.get('/category/{CateId}')
def cate_goods_list(CateId: str, db: Session = Depends(get_db)):
    if CateId in ['01', '02', '03', '04', '05']:
        result = get_cate_goods_list(CateId, db)

        if len(result) == 0:
            catename = db.query(Cate_1.name)\
                .where(Cate_1.id_ == '01').one()
        
            return {
                'n_goods' : 0,
                'category' : [{'id':CateId, 'name': catename[0]}],
                'detail' : []
            }
        else:
        
            return {
                'n_goods' : len(result),
                'category' : [{'id':CateId, 'name': result[0][-1]}],
                'goods' : [{'id':i, 'name': n, 'price':p, 'img_url':u} for i, n, p, u, _ in result]
            }
        
    else:
        raise HTTPException(status_code=404, detail="Category not found") 