"""add_link_in_eduacation_material

Revision ID: 99753bc733e3
Revises: dafba4de0693
Create Date: 2025-01-19 05:00:50.481018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99753bc733e3'
down_revision: Union[str, None] = 'dafba4de0693'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('educational_material', sa.Column('link_to_picture', sa.String(), nullable=True))
    op.add_column('educational_material', sa.Column('number', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('educational_material', 'link_to_picture')
    op.drop_column('educational_material', 'number')
