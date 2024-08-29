"""add new column user_recommendation

Revision ID: 0306faf68636
Revises: ac30af0da387
Create Date: 2024-08-30 04:01:27.469675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0306faf68636'
down_revision: Union[str, None] = 'ac30af0da387'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)

    # Проверяем, существует ли колонка
    columns = inspector.get_columns('borders')
    if 'user_recommendation' not in [column['name'] for column in columns]:
        op.add_column('borders', sa.Column('user_recommendation', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('borders', 'user_recommendation')
