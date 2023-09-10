"""empty message

Revision ID: 2e9d64e3b749
Revises: 
Create Date: 2023-09-10 13:03:38.117974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e9d64e3b749'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('car_inventory',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('make', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('top_speed', sa.String(length=50), nullable=True),
    sa.Column('_range', sa.String(length=50), nullable=True),
    sa.Column('fast_charge', sa.String(length=50), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car_inventory')
    op.drop_table('user')
    # ### end Alembic commands ###
