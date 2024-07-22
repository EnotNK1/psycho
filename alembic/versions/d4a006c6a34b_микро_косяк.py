"""Микро косяк

Revision ID: d4a006c6a34b
Revises: b0626ce69749
Create Date: 2024-07-22 17:45:06.944339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4a006c6a34b'
down_revision: Union[str, None] = 'b0626ce69749'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
