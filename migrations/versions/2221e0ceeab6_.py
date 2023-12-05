"""empty message

Revision ID: 2221e0ceeab6
Revises: 254052792c20
Create Date: 2023-12-05 11:37:05.241348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2221e0ceeab6'
down_revision = '254052792c20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ac', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_column('ac')

    # ### end Alembic commands ###
