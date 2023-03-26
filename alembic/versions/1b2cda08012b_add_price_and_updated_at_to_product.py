"""add price and updated_at to product

Revision ID: 1b2cda08012b
Revises: 
Create Date: 2023-03-26 13:54:08.951123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b2cda08012b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('product', sa.Column('price', sa.NUMERIC))
    op.add_column('product', sa.Column('updated_at', sa.DateTime))



def downgrade() -> None:
    pass
