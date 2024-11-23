"""add last few columns to posts table

Revision ID: 0a158fd71f38
Revises: 3e22b7ed9e25
Create Date: 2024-11-23 13:29:50.185745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a158fd71f38'
down_revision: Union[str, None] = '3e22b7ed9e25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default= "TRUE"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default= sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
