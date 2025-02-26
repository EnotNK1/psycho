from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b1f87891410e'
down_revision: Union[str, None] = '0d90465acb34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('educational_card',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('link_to_picture', sa.String(), nullable=True),
    sa.Column('educational_material_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['educational_material_id'], ['educational_material.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    op.drop_table('educational_card')
