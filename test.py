# -*- coding: utf-8 -*-
import logging

from models import Product, Review
from database import SessionLocal
from datetime import datetime


db = SessionLocal()

try:

    print(db.query(Review).all())
    db.commit()

except Exception as e:
    print("An error occurred:", e)
    db.rollback()

finally:
    # 세션 닫기
    db.close()
