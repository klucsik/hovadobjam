"""init

Revision ID: b2e123ae6047
Revises: 
Create Date: 2019-09-30 20:58:30.160532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2e123ae6047'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hull_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alias_name'), 'alias', ['name'], unique=True)
    op.create_table('hullinfo',
    sa.Column('hull_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('hull_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('kuka',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_kuka_name'), 'kuka', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('hogyan_dobjam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hull_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=500), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hull_id'], ['hullinfo.hull_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_hova_dobta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hull_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('kuka_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hull_id'], ['hullinfo.hull_id'], ),
    sa.ForeignKeyConstraint(['kuka_id'], ['kuka.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hogyan_dobjam_scores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('increment', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['hogyan_dobjam.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hogyan_dobjam_scores')
    op.drop_table('user_hova_dobta')
    op.drop_table('hogyan_dobjam')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_kuka_name'), table_name='kuka')
    op.drop_table('kuka')
    op.drop_table('hullinfo')
    op.drop_index(op.f('ix_alias_name'), table_name='alias')
    op.drop_table('alias')
    # ### end Alembic commands ###
