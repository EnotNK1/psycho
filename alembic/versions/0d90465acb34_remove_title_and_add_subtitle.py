from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0d90465acb34'
down_revision: Union[str, None] = '395d7eb666c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавление столбца subtitle
    op.add_column('educational_material', sa.Column('subtitle', sa.String(), nullable=True))
    op.drop_column('educational_material', 'text')
    op.add_column('educational_theme', sa.Column('related_topics', sa.JSON, nullable=True))

def downgrade() -> None:
    # Удаление столбца subtitle
    op.drop_column('educational_material', 'subtitle')
    op.add_column('educational_material', sa.Column('text', sa.String(), nullable=True))
    op.drop_column('educational_theme', 'related_topics')