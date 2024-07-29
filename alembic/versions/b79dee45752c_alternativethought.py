"""alternativethought

Revision ID: b79dee45752c
Revises: cc90352cf4f0
Create Date: 2024-07-29 18:13:40.204588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b79dee45752c'
down_revision: Union[str, None] = 'cc90352cf4f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
