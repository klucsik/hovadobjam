"""pic

Revision ID: a7a42978abff
Revises: b2e123ae6047
Create Date: 2019-09-30 22:21:35.165904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7a42978abff'
down_revision = 'b2e123ae6047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hullinfo', sa.Column('picurl', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hullinfo', 'picurl')
    # ### end Alembic commands ###
