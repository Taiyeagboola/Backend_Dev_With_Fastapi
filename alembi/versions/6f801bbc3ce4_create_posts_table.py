"""create posts table

Revision ID: 6f801bbc3ce4
Revises: 
Create Date: 2025-12-05 09:13:31.748164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f801bbc3ce4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
