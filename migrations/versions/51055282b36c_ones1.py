"""ones1

Revision ID: 51055282b36c
Revises: 0b267bcbcdf2
Create Date: 2019-04-25 11:48:49.443381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51055282b36c'
down_revision = '0b267bcbcdf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'c')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('c', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    # ### end Alembic commands ###