"""Исправлена связь ползователя и задачи

Revision ID: b0626ce69749
Revises: bda60fc30d52
Create Date: 2024-07-22 17:43:10.855727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0626ce69749'
down_revision: Union[str, None] = 'bda60fc30d52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
