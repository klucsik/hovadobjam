"""empty message

Revision ID: d7a42ada3d83
Revises: f2fcd209f017
Create Date: 2019-10-11 17:59:02.359288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7a42ada3d83'
down_revision = 'f2fcd209f017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('refresh', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('token', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token')
    op.drop_column('user', 'refresh')
    # ### end Alembic commands ###
