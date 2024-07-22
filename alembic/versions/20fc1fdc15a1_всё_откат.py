"""Всё откат

Revision ID: 20fc1fdc15a1
Revises: d4a006c6a34b
Create Date: 2024-07-22 17:49:14.909895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20fc1fdc15a1'
down_revision: Union[str, None] = 'd4a006c6a34b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
