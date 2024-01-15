"""row channel unique

Revision ID: fedb609abe1b
Revises: c5d82f4313fa
Create Date: 2024-01-12 15:33:17.460325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fedb609abe1b'
down_revision: Union[str, None] = 'c5d82f4313fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_channels_channel', table_name='channels')
    op.create_index(op.f('ix_channels_channel'), 'channels', ['channel'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_channels_channel'), table_name='channels')
    op.create_index('ix_channels_channel', 'channels', ['channel'], unique=False)
    # ### end Alembic commands ###
