"""test

Revision ID: 7ea6f8dd1ad3
Revises: 20fc1fdc15a1
Create Date: 2024-07-29 18:04:08.293576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ea6f8dd1ad3'
down_revision: Union[str, None] = '20fc1fdc15a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
