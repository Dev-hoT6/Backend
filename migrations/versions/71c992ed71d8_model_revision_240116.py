"""model revision 240116

Revision ID: 71c992ed71d8
Revises: 
Create Date: 2024-01-16 02:49:25.187978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71c992ed71d8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CATE1',
    sa.Column('CateId', sa.String(length=2), nullable=False),
    sa.Column('CateName', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('CateId'),
    sa.UniqueConstraint('CateId')
    )
    op.create_table('CATE2',
    sa.Column('CateId', sa.String(length=2), nullable=False),
    sa.Column('CateName', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('CateId'),
    sa.UniqueConstraint('CateId')
    )
    op.create_table('PRODUCT',
    sa.Column('ProdId', sa.String(length=7), nullable=False),
    sa.Column('ProdName', sa.String(length=50), nullable=False),
    sa.Column('ProdImgPath', sa.String(), nullable=True),
    sa.Column('ProdImgUrl', sa.String(), nullable=True),
    sa.Column('ProdPrice', sa.Integer(), nullable=False),
    sa.Column('ProdCategory1', sa.String(length=2), nullable=False),
    sa.Column('ProdCategory2', sa.String(length=2), nullable=True),
    sa.Column('ProdDescription', sa.String(length=200), nullable=False),
    sa.Column('Hashtag', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('ProdId'),
    sa.UniqueConstraint('ProdId')
    )
    op.create_table('VECTORS',
    sa.Column('RevId', sa.String(length=6), nullable=False),
    sa.Column('Vector', sa.PickleType(), nullable=False),
    sa.PrimaryKeyConstraint('RevId'),
    sa.UniqueConstraint('RevId')
    )
    op.create_table('REVIEW',
    sa.Column('RevId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ProdId', sa.String(length=6), nullable=False),
    sa.Column('Writer', sa.String(length=4), nullable=False),
    sa.Column('RevImgPath', sa.String(), nullable=True),
    sa.Column('RevImgUrl', sa.String(), nullable=True),
    sa.Column('Content', sa.String(length=300), nullable=False),
    sa.Column('Points', sa.Integer(), nullable=True),
    sa.Column('Status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ProdId'], ['PRODUCT.ProdId'], ),
    sa.PrimaryKeyConstraint('RevId')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('REVIEW')
    op.drop_table('VECTORS')
    op.drop_table('PRODUCT')
    op.drop_table('CATE2')
    op.drop_table('CATE1')
    # ### end Alembic commands ###
