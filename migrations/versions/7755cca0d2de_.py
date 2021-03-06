"""empty message

Revision ID: 7755cca0d2de
Revises: 44d4ebb4a477
Create Date: 2018-08-23 15:29:22.986372

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7755cca0d2de'
down_revision = '44d4ebb4a477'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('txt')
    op.add_column('users_txt', sa.Column('text_id', sa.Integer(), nullable=True))
    op.drop_constraint('users_txt_ibfk_1', 'users_txt', type_='foreignkey')
    op.create_foreign_key(None, 'users_txt', 'text', ['text_id'], ['id'])
    op.drop_column('users_txt', 'txt_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_txt', sa.Column('txt_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users_txt', type_='foreignkey')
    op.create_foreign_key('users_txt_ibfk_1', 'users_txt', 'txt', ['txt_id'], ['id'])
    op.drop_column('users_txt', 'text_id')
    op.create_table('txt',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('text', mysql.TEXT(collation='utf8_unicode_ci'), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('text')
    # ### end Alembic commands ###
