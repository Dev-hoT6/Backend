######## DB 초기화 후 데이터 주입용 파일

import sqlite3
import pandas as pd
import os

db_name = 'myapi.db'

product = 'data_prototype/product.csv'
review = 'data_prototype/reviews.csv'
cate1 = 'data_prototype/cate_1.csv'
cate2 = 'data_prototype/cate_2.csv',
# vectors = 'data_prototype/vectors.csv',

product = pd.read_csv(product,
                     dtype={'ProdId':str, 'ProdName':str, 'ProdPrice':int, 'ProdCategory1':str}
                     )
review = pd.read_csv(review,
                     dtype={'RevId':str, 'ProdId':str}
                     )
cate1 = pd.read_csv(cate1,
                     dtype={'CateId':str, 'CateName':str}
                     )
cate_2 = pd.read_csv(cate_2,
                     dtype={'CateId':str, 'CateName':str}
                     )


data_list = [
    product, 
    review,
    cate1,
    cate2,
    # vectors
]

table_list = [
    'PRODUCT',
    'REVIEW',
    'CATE1',
    'CATE2',
    # 'VECTORS'
]
# def get_data(sql, db):
#     with sqlite3.connect(db) as con:
#         cursor = con.cursor()
#         cursor.execute(sql)
#     return cursor.fetchall()

def insert_data(data, db, tablename, if_exists='append'):
    with sqlite3.connect(db) as con:
        data.to_sql(name=tablename, if_exists=if_exists, con=con, index=False)
        # print(get_data('SELECT * FROM {}'.format(tablename), db))
    print('{} Data Successfully Inserted'.format(len(data)))

if __name__ == '__main__':
    for data, table_name in zip(data_list, table_list):
        insert_data(data, db_name, table_name)
