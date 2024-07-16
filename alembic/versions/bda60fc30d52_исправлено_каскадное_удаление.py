"""Исправлено каскадное удаление

Revision ID: bda60fc30d52
Revises: 42ce2cb00e0e
Create Date: 2024-07-17 01:04:56.853575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bda60fc30d52'
down_revision: Union[str, None] = '42ce2cb00e0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
