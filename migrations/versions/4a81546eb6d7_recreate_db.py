"""recreate db

Revision ID: 4a81546eb6d7
Revises: 0cb0b30c7a56
Create Date: 2023-03-09 06:54:02.769331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a81546eb6d7'
down_revision = '0cb0b30c7a56'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(), nullable=True))
    op.drop_column('user', 'user_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_name', sa.VARCHAR(), nullable=True))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###