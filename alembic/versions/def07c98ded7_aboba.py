"""aboba

Revision ID: def07c98ded7
Revises: 48416b6d7b52
Create Date: 2024-07-29 19:06:49.642841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'def07c98ded7'
down_revision: Union[str, None] = '48416b6d7b52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('diary_record')]

    if 'alternativeThought' in columns:
        op.alter_column('diary_record', 'alternativeThought', new_column_name='alternative_thought')


def downgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('diary_record')]

    if 'alternative_thought' in columns:
        op.alter_column('diary_record', 'alternative_thought', new_column_name='alternativeThought')
