"""posts table

Revision ID: 4b17f39d41e1
Revises: e0333bd61410
Create Date: 2021-08-25 15:11:04.725695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b17f39d41e1'
down_revision = 'e0333bd61410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('body', sa.String(length=140), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
