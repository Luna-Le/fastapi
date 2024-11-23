"""add content column to posts table

Revision ID: c923dc2db084
Revises: 4545eca0711c
Create Date: 2024-11-23 13:01:41.274147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c923dc2db084'
down_revision: Union[str, None] = '4545eca0711c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
