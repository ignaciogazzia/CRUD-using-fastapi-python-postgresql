"""add index to products and relation to clients

Revision ID: 52ef792a8690
Revises: 1b2cda08012b
Create Date: 2023-03-28 01:02:48.073324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52ef792a8690'
down_revision = '1b2cda08012b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('clients',
                    sa.Column('client_id', sa.NUMERIC, primary_key=True),
                    sa.Column('client_name', sa.String(20), nullable=False, index=True),
                    sa.Column('is_active', sa.Boolean, nullable=False),
                    sa.Column('country_id', sa.NUMERIC, nullable=False),
                    sa.Column('created_at',  sa.DateTime),
                    sa.Column('updated_at', sa.DateTime)
                    )
    op.create_index('product_name_index', 'product', ['title'])
    op.add_column('product', sa.Column('is_active', sa.Boolean))


def downgrade() -> None:
    pass
