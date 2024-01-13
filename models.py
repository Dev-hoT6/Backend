from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Product(Base):
    __tablename__ = "product"

    # primary_key=True
    id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column(String)
    img_url = Column(String)
    price = Column(Integer)
    # "Electronics, Gadgets" 이런식으로 문자열로 리스트를 만든다.
    category = Column(String)
    description = Column(String)
    hashtag = Column(String)

class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    #question의 id 컬럼과 연계 된다는 의미
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", backref="answers")
# {
#   "squadName": "Super hero squad",
#   "homeTown": "Metro City",
#   "formed": 2016,
#   "secretBase": "Super tower",
#   "active": true,
#   "members": [
#     {
#       "name": "Molecule Man",
#       "age": 29,
#       "secretIdentity": "Dan Jukes",
#       "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
#     },
#     {
#       "name": "Madame Uppercut",
#       "age": 39,
#       "secretIdentity": "Jane Wilson",
#       "powers": [
#         "Million tonne punch",
#         "Damage resistance",
#         "Superhuman reflexes"
#       ]
#     },