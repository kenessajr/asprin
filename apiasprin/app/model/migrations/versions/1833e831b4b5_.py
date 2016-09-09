"""empty message

Revision ID: 1833e831b4b5
Revises: bc59f1246e2d
Create Date: 2016-09-07 10:06:52.883538

"""

# revision identifiers, used by Alembic.
revision = '1833e831b4b5'
down_revision = 'bc59f1246e2d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gender', sa.String(length=10), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'gender')
    ### end Alembic commands ###