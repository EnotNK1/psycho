"""rename_column

Revision ID: 48416b6d7b52
Revises: b79dee45752c
Create Date: 2024-07-29 18:24:42.474928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48416b6d7b52'
down_revision: Union[str, None] = 'b79dee45752c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
