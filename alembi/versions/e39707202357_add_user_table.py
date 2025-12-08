"""add user table

Revision ID: e39707202357
Revises: dc10de35d5ed
Create Date: 2025-12-05 10:17:31.582755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e39707202357'
down_revision: Union[str, Sequence[str], None] = 'dc10de35d5ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False),sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
