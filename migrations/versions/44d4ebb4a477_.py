"""empty message

Revision ID: 44d4ebb4a477
Revises: 8ccc20e99531
Create Date: 2018-08-23 15:20:10.321762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44d4ebb4a477'
down_revision = '8ccc20e99531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('txt', sa.Column('name', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('txt', 'name')
    # ### end Alembic commands ###
