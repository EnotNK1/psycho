"""Изменен тип данных score с int на float

Revision ID: ac30af0da387
Revises: 1d3e99262650
Create Date: 2024-08-12 17:34:07.178707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac30af0da387'
down_revision: Union[str, None] = '1d3e99262650'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('scale_result')

    for column in columns:
        if column['name'] == 'score' and not isinstance(column['type'], sa.Float):
            op.alter_column(
                'scale_result',
                'score',
                type_=sa.Float(),
                existing_type=column['type'],
                existing_nullable=False
            )


def downgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('scale_result')

    for column in columns:
        if column['name'] == 'score' and not isinstance(column['type'], sa.Integer):
            op.alter_column(
                'scale_result',
                'score',
                type_=sa.Integer(),
                existing_type=column['type'],
                existing_nullable=False
            )
