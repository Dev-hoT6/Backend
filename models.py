from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Product(Base):
    __tablename__ = "PRODUCT"

    id_ = Column('ProdId', String(6), primary_key=True, unique=True)
    name = Column('ProdName', String(50), nullable=False)
    img_path = Column('ProdImgPath', String)
    img_url = Column('ProdImgUrl', String)
    price = Column('ProdPrice', Integer, nullable=False)
    cate1 = Column('ProdCategory1', String(2), nullable=False)
    cate2 = Column('ProdCategory2', String(2))
    description = Column('ProdDescription', String(200), nullable=False)
    hashtag = Column('Hashtag', String(200)) # 띄어쓰기로 구분


class Review(Base):
    __tablename__ = "REVIEW"

    id_ = Column('RevId', String(8), primary_key=True, unique=True)
    prod_id = Column('ProdId', String(6), ForeignKey('PRODUCT.ProdId'), nullable=False)
    writer = Column('Writer', String(4), nullable=False)
    img_path = Column('RevImgPath', String)
    img_url = Column('RevImgUrl', String)
    content = Column('Content', String(300), nullable=False)
    points = Column('Points', Integer, default=0)
    status = Column('Status', Integer, default=0)

    products = relationship('PRODUCT', backref='reviews')


class Cate_1(Base):
    __tablename__ = "CATE1"

    id_ = Column('CateId', String(2), primary_key=True, unique=True)
    name = Column('CateName', String(10), nullable=False)


class Cate_2(Base):
    __tablename__ = "CATE2"

    id_ = Column('CateId', String(2), primary_key=True, unique=True)
    name = Column('CateName', String(10), nullable=False)


class Vectors(Base):
    __tablename__ = "VECTORS"

    id_ = Column('RevId', String(6), primary_key=True, unique=True)
    vector = Column('Vector', LargeBinary(), nullable=False)