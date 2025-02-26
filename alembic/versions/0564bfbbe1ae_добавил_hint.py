from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0564bfbbe1ae'
down_revision: Union[str, None] = '395d7eb666c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавляем новый столбец hint
    op.add_column('field', sa.Column('hint', sa.String(), nullable=True))

    op.alter_column('field', 'title', nullable=True)

    # Переносим данные из title в hint
    # op.execute(f"UPDATE {'field'} SET hint = title")

    # Очищаем поле title (ранее title)
    # op.execute(f"UPDATE {'field'} SET title = NULL")


def downgrade() -> None:
    # Восстанавливаем данные обратно
    # op.execute(f"UPDATE {'field'} SET title = hint")

    # Удаляем поле hint
    op.drop_column('field', 'hint')

    op.alter_column('field', "title", nullable=False)
