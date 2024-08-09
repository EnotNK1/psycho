"""Изменен тип данных границы в borders с int на float

Revision ID: 1d3e99262650
Revises: def07c98ded7
Create Date: 2024-08-09 20:02:36.793993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d3e99262650'
down_revision: Union[str, None] = 'def07c98ded7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('borders', 'left_border',
                    type_=sa.Float(),
                    existing_type=sa.Integer(),
                    existing_nullable=False)
    op.alter_column('borders', 'right_border',
                    type_=sa.Float(),
                    existing_type=sa.Integer(),
                    existing_nullable=False)


def downgrade() -> None:
    op.alter_column('borders', 'left_border',
                    type_=sa.Integer(),
                    existing_type=sa.Float(),
                    existing_nullable=False)
    op.alter_column('borders', 'right_border',
                    type_=sa.Integer(),
                    existing_type=sa.Float(),
                    existing_nullable=False)
