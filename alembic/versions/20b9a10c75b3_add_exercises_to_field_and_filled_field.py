"""add_exercises_to_field_and_filled_field

Revision ID: 20b9a10c75b3
Revises: db411a33e733
Create Date: 2025-03-04 16:14:43.784149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '20b9a10c75b3'
down_revision: Union[str, None] = 'db411a33e733'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('field', sa.Column('exercises', postgresql.ARRAY(sa.String()), nullable=True))
    op.add_column('filled_field', sa.Column('exercises', postgresql.ARRAY(sa.String()), nullable=True))


def downgrade() -> None:
    op.drop_column('filled_field', 'exercises')
    op.drop_column('field', 'exercises')