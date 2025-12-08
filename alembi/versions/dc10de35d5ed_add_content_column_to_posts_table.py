"""add content column to posts table

Revision ID: dc10de35d5ed
Revises: 6f801bbc3ce4
Create Date: 2025-12-05 09:49:46.745393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc10de35d5ed'
down_revision: Union[str, Sequence[str], None] = '6f801bbc3ce4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
