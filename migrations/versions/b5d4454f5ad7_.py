"""empty message

Revision ID: b5d4454f5ad7
Revises: 
Create Date: 2023-12-10 22:10:30.846748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5d4454f5ad7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player_alignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('player_alignment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_alignment_name'), ['name'], unique=False)

    op.create_table('player_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('hit_die', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('player_class', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_class_name'), ['name'], unique=False)

    op.create_table('player_race',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('player_race', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_race_name'), ['name'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('pw_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('campaign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=4096), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    with op.batch_alter_table('campaign', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_campaign_name'), ['name'], unique=True)

    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('gender', sa.String(length=128), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('str', sa.Integer(), nullable=True),
    sa.Column('dex', sa.Integer(), nullable=True),
    sa.Column('con', sa.Integer(), nullable=True),
    sa.Column('int', sa.Integer(), nullable=True),
    sa.Column('wis', sa.Integer(), nullable=True),
    sa.Column('cha', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('xp', sa.Integer(), nullable=True),
    sa.Column('ac', sa.Integer(), nullable=True),
    sa.Column('spd', sa.Integer(), nullable=True),
    sa.Column('hp', sa.Integer(), nullable=True),
    sa.Column('hp_max', sa.Integer(), nullable=True),
    sa.Column('insp', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=4096), nullable=True),
    sa.Column('player_class', sa.Integer(), nullable=False),
    sa.Column('player_race', sa.Integer(), nullable=False),
    sa.Column('player_alignment', sa.Integer(), nullable=False),
    sa.Column('player_campaign', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_alignment'], ['player_alignment.id'], ),
    sa.ForeignKeyConstraint(['player_campaign'], ['campaign.id'], ),
    sa.ForeignKeyConstraint(['player_class'], ['player_class.id'], ),
    sa.ForeignKeyConstraint(['player_race'], ['player_race.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_gender'), ['gender'], unique=False)
        batch_op.create_index(batch_op.f('ix_player_name'), ['name'], unique=False)

    op.create_table('user_to_player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_to_player')
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_name'))
        batch_op.drop_index(batch_op.f('ix_player_gender'))

    op.drop_table('player')
    with op.batch_alter_table('campaign', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_campaign_name'))

    op.drop_table('campaign')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    with op.batch_alter_table('player_race', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_race_name'))

    op.drop_table('player_race')
    with op.batch_alter_table('player_class', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_class_name'))

    op.drop_table('player_class')
    with op.batch_alter_table('player_alignment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_alignment_name'))

    op.drop_table('player_alignment')
    # ### end Alembic commands ###