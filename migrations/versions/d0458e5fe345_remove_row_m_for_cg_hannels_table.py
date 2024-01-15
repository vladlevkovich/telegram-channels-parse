"""remove row m for cg=hannels table

Revision ID: d0458e5fe345
Revises: a3e2f892a938
Create Date: 2024-01-12 17:32:23.981110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0458e5fe345'
down_revision: Union[str, None] = 'a3e2f892a938'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('channels', 'm')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('m', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
