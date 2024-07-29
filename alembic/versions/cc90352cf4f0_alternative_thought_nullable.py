"""alternative_thought_nullable

Revision ID: cc90352cf4f0
Revises: 7ea6f8dd1ad3
Create Date: 2024-07-29 18:06:56.910199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc90352cf4f0'
down_revision: Union[str, None] = '7ea6f8dd1ad3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
